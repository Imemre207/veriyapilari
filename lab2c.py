import pandas as pd
import matplotlib.pyplot as plt
import io
import subprocess
import re


# lab02.exe dosyasını çalıştır ve çıktıyı al
result = subprocess.run(['./lab02.exe'], capture_output=True, text=True)

# Çıktıyı satırlara ayır
output_lines = result.stdout.strip().split('\n')

# Listeyi string'e dönüştür
output_string = '\n'.join(output_lines)

# StringIO kullanarak çıktıyı bir dosya gibi okuyoruz
df = pd.read_csv(io.StringIO(output_string), sep='\t')

# 'Size' sütununu index olarak ayarlıyoruz
df.set_index('Size', inplace=True)

# Grafiği oluşturuyoruz
plt.figure(figsize=(12, 6))
plt.plot(df.index, df[df.columns[0]], label=df.columns[0], marker='o')
plt.plot(df.index, df[df.columns[1]], label=df.columns[1], marker='s')

#plt.xscale('log')  # x eksenini logaritmik ölçeğe ayarlıyoruz
#plt.yscale('log')  # y eksenini logaritmik ölçeğe ayarlıyoruz

plt.xlabel('Dizi Boyutu')
plt.ylabel('Çalışma Süresi (saniye)')
plt.title('Fonksiyon 1 ve Basamak Toplamı Fonksiyonlarının Big-O Grafikleri (C dili)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)

plt.tight_layout()
plt.show()
