import pandas as pd
import geopandas as gpd

def load_csv(path):
    """Membaca file CSV dengan penanganan error dasar."""
    try:
        df = pd.read_csv(path)
        print(f"Sukses memuat: {path} | Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"ERROR: File tidak ditemukan di {path}")
    except Exception as e:
        print(f"ERROR: Gagal memuat file: {e}")

def load_shapefile(path, target_crs="EPSG:4326"):
    """Membaca Shapefile/GeoJSON dan mengkonversi CRS."""
    try:
        gdf = gpd.read_file(path)
        print(f"Sukses memuat: {path} | CRS Awal: {gdf.crs}")
        if gdf.crs != target_crs:
            gdf = gdf.to_crs(target_crs)
            print(f"Sukses konversi CRS ke {target_crs}")
        return gdf
    except FileNotFoundError:
        print(f"ERROR: File tidak ditemukan di {path}")
    except Exception as e:
        print(f"ERROR: Gagal memuat file: {e}")

if __name__ == '__main__':
    # Contoh penggunaan
    df_data = load_csv('data/data_ikan.csv')
    gdf_peta = load_shapefile('data/peta_konservasi.shp')
    
    if df_data is not None:
        print("\nInspeksi Data CSV:")
        print(df_data.info())
    
    if gdf_peta is not None:
        print("\nInspeksi Data Peta:")
        print(gdf_peta.head())
