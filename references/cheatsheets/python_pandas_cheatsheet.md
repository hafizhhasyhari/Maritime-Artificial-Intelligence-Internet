# Ringkasan: Pandas
import pandas as pd

# Membaca Data
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_sql('query', conn)

# Inspeksi Dasar
df.head(5)        # 5 baris pertama
df.tail(5)        # 5 baris terakhir
df.info()         # Tipe data, memori, nilai null
df.describe()     # Statistik dasar (mean, std, min, max)
df.shape          # (jumlah_baris, jumlah_kolom)
df.columns        # Daftar nama kolom
df['kolom'].unique() # Nilai unik di kolom
df['kolom'].value_counts() # Hitung nilai unik

# Seleksi (Indexing)
df['kolom']             # Satu kolom (Series)
df[['kolom1', 'kolom2']] # Beberapa kolom (DataFrame)
df.loc[0]               # Seleksi by label (baris ke-0)
df.loc[0:5, 'kolom1']   # Iris baris dan kolom by label
df.iloc[0]              # Seleksi by posisi (baris ke-0)
df.iloc[0:5, 0:2]       # Iris baris dan kolom by posisi

# Filtering (Masking)
df[df['umur'] > 25]
df[df['negara'] == 'Indonesia']
df[df['kolom'].isin(['A', 'B'])]

# Manipulasi
df['kolom_baru'] = df['kolom1'] + df['kolom2']
df = df.drop('kolom_jelek', axis=1) # Hapus kolom
df = df.drop(0, axis=0) # Hapus baris
df = df.rename(columns={'nama_lama': 'nama_baru'})

# Data Hilang (Missing Data)
df.isnull().sum() # Hitung NaN per kolom
df = df.dropna()  # Buang baris dgn NaN
df = df.fillna(0) # Isi NaN dgn 0
df['kolom'] = df['kolom'].fillna(df['kolom'].mean()) # Isi dgn mean

# GroupBy (Penting!)
df.groupby('negara')['populasi'].sum()
df.groupby(['negara', 'tahun'])['gdp'].mean()
df.groupby('grup').agg({'kolom1': 'mean', 'kolom2': 'sum'})

# Menggabung (Merge/Join)
pd.merge(df1, df2, on='id_kunci')
pd.merge(df1, df2, left_on='id_A', right_on='id_B')
pd.concat([df1, df2]) # Menumpuk (baris)
