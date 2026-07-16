import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 0. MEMBUAT FOLDER OUTPUT OTOMATIS
# Langkah ini memastikan folder 'output' langsung terbuat saat program dijalankan
if not os.path.exists('output'):
    os.makedirs('output')
    print("[INFO] Folder 'output' berhasil dibuat otomatis.")

# 1. LOAD DATASET
# Membaca data film dari file CSV yang sudah disiapkan
try:
    df = pd.read_csv('movie_data.csv')
    print("[INFO] Dataset berhasil dimuat.\n")
except FileNotFoundError:
    print("[ERROR] File 'movie_data.csv' tidak ditemukan! Pastikan posisinya satu folder dengan main.py")
    exit()

# 2. CORE ML: RULE-BASED ENGINE (Decision Tree Manual)
# Aturan: Jika Genre-nya 'Action' atau 'Drama' DAN Rating-nya >= 8.5, 
# maka statusnya 'Sangat Direkomendasikan'. Jika tidak, 'Biasa Saja'.
kondisi = ((df['Genre'] == 'Action') | (df['Genre'] == 'Drama')) & (df['Rating'] >= 8.5)
df['Rekomendasi_Status'] = np.where(kondisi, 'Sangat Direkomendasikan', 'Biasa Saja')

# 3. REKAPITULASI & MENAMPILKAN HASIL (Pandas)
print("="*40)
print("        HASIL PREDIKSI REKOMENDASI        ")
print("="*40)
print(df[['Title', 'Genre', 'Rating', 'Rekomendasi_Status']])
print("\n" + "="*40)
print("       RINGKASAN DISTRIBUSI DATA         ")
print("="*40)
print(df['Rekomendasi_Status'].value_counts())

# 4. VISUALISASI DATA (Matplotlib & Ekspor ke Folder Output)
plt.figure(figsize=(6, 4))
df['Rekomendasi_Status'].value_counts().plot(kind='bar', color=['#ff7f0e', '#1f77b4'])
plt.title('Grafik Distribusi Hasil Rekomendasi Film')
plt.xlabel('Status Rekomendasi')
plt.ylabel('Jumlah Film')
plt.xticks(rotation=0)

# Menyimpan grafik secara otomatis ke dalam folder output sesuai ketentuan
grafik_path = 'output/grafik_rekomendasi.png'
plt.savefig(grafik_path, bbox_inches='tight', dpi=300)
plt.close()

print(f"\n[SUKSES] Grafik visualisasi berhasil diekspor ke: {grafik_path}")
print("="*40)