# Ringkasan: GeoPandas
import geopandas as gpd

# Membaca Data
gdf = gpd.read_file('data.shp')
gdf = gpd.read_file('data.geojson')

# Inspeksi Dasar
gdf.head()
gdf.info()
gdf.plot()          # Plot sederhana (mudah!)
gdf.crs             # Cek Coordinate Reference System
gdf['geometry']     # Kolom geometri
gdf.total_bounds    # Batas (x_min, y_min, x_max, y_max)

# CRS (PENTING!)
gdf.crs                 # Cek CRS (misal: EPSG:4326)
gdf = gdf.to_crs(epsg=4326) # Konversi ke WGS84 (Lat/Lon)
gdf = gdf.to_crs(epsg=32748) # Konversi ke UTM (Meter)

# Atribut Geometri
gdf['geometry'].area          # Menghitung area (pastikan CRS dalam meter!)
gdf['geometry'].length        # Menghitung panjang (pastikan CRS dalam meter!)
gdf['geometry'].centroid      # Mendapatkan titik tengah
gdf['geometry'].buffer(100)   # Membuat buffer (misal: 100 meter)

# Operasi Spasial
titik = Point(lon, lat)
polygon = Polygon([...])
gdf_baru = gpd.GeoDataFrame(data, geometry=[...])

# Analisis (Query) Spasial
gpd.sjoin(gdf_titik, gdf_poligon, op='within') # Titik mana yg ada di dlm poligon
gpd.sjoin(gdf_A, gdf_B, op='intersects')     # Poligon mana yg bersinggungan

# Gabung Data (Join)
# Menggabungkan data spasial (geopandas) dgn data tabular (pandas)
gdf_merged = gdf.merge(df_pandas, on='id_kunci')

# Menyimpan Data
gdf.to_file('hasil.geojson', driver='GeoJSON')
gdf.to_file('hasil.shp', driver='ESRI Shapefile')
