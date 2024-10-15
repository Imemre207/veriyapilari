import matplotlib.pyplot as plt
import pandas as pd
import time
import random

def loop(N):
    toplam=0
    for i in range(N):
        for j in range(N):
            toplam=toplam+1
    return toplam

def kare_toplami(N):
    toplam=0
    for i in range(1,N+1):
        toplam+=i*i
    return toplam


def measure_time(algorithm, input_data):
    start_time = time.time()
    algorithm(input_data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def generate_random_list(length):
    random_list = [random.randint(1, 100) for _ in range(length)]
    return random_list

experiment_sizes = [1, 10, 100, 1000, 10000,100000]
experiment_results = []

for size in experiment_sizes:
    input_list = generate_random_list(size)
    loop_time = measure_time(loop,size)
    kare_time = measure_time(kare_toplami,size)
    
    experiment_results.append((size, loop_time,kare_time))

# DataFrame oluşturma
df = pd.DataFrame(experiment_results, columns=['Size', 'İkili Döngü','Kare Toplam'])

# 'Size' sütununu index olarak ayarlama
df.set_index('Size', inplace=True)

# DataFrame'i yazdırma
df

# Grafiği oluşturuyoruz
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['İkili Döngü'], label='İkili Döngü', marker='o')
plt.plot(df.index, df['Kare Toplam'], label='Kare Toplam', marker='s')

#plt.xscale('log')  # x eksenini logaritmik ölçeğe ayarlıyoruz
#plt.yscale('log')  # y eksenini logaritmik ölçeğe ayarlıyoruz

plt.xlabel('Dizi Boyutu')
plt.ylabel('Çalışma Süresi (saniye)')
plt.title('İkili Döngünün ve Tekli Döngünü Big-O Grafiklerinin Karşılaştırması')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.2)

plt.tight_layout()
plt.show()