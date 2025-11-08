import folium
import geopandas as gpd

# 1. Buat Peta Dasar
# Mulai dari koordinat tengah Indonesia
m = folium.Map(location=[-2.5, 118.0], zoom_start=5)

# 2. Tambah Data Titik (dari CSV/Pandas)
# Asumsi Anda punya df_lokasi (lat, lon, nama)
# for idx, row in df_lokasi.iterrows():
#     folium.Marker(
#         location=[row['lat'], row['lon']],
#         popup=f"<strong>{row['nama']}</strong><br>{row['info_tambahan']}",
#         tooltip=row['nama'],
#         icon=folium.Icon(color='blue', icon='info-sign')
#     ).add_to(m)

# 3. Tambah Data Poligon (dari GeoJSON/Geopandas)
# Asumsi Anda punya gdf_area (geometry, nama_area)
try:
    gdf_area = gpd.read_file('data/peta_area_konservasi.geojson')
    
    folium.GeoJson(
        gdf_area,
        name='Area Konservasi',
        style_function=lambda feature: {
            'fillColor': 'green',
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.5,
        },
        tooltip=folium.GeoJsonTooltip(fields=['nama_area'], aliases=['Nama:'])
    ).add_to(m)
    print("Sukses menambah layer GeoJSON.")

except Exception as e:
    print(f"Gagal menambah layer GeoJSON: {e}")
    # Tambah data titik manual jika file tidak ada
    folium.Marker(
        location=[-6.175, 106.827],
        popup="Contoh: Monas",
        icon=folium.Icon(color='red')
    ).add_to(m)


# 4. Tambah Kontrol Layer
folium.LayerControl().add_to(m)

# 5. Simpan Peta ke HTML
output_file = 'peta_interaktif.html'
m.save(output_file)
print(f"Peta berhasil disimpan ke {output_file}")
