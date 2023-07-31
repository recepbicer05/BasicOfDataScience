#Python ile Veri Analizi
# -Numpy -Pandas -Veri Görselleştirme: Matplotlib & Seaborn - Gelişmiş Fonksiyonel Keşifçi Veri Analizi

# NumPy = Numerical Python

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

print(a*b)

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

print(np.zeros(10, dtype=float))

print(np.random.randint(0, 10, size=10))

print(np.random.normal(10, 4, [3,4]))# 3 satır ve 4 sütündan oluşan, ortalaması 10 standart sapması 4 bir çıktı aldık.

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

v = np.random.randint(0, 10, size=9).reshape(3, 3) # reshape ile şeklini değiştirdik.

print(v)
print(v.ndim, v.shape, v.size, v.dtype)

# FancyIndex

z = np.arange(0, 30, 3)

catch = [2, 5, 8] # indeksleri buraya girip z arrayinin içindeki değerleri tuttuk.

print(z[catch])

i = np.array([1, 2, 3, 4, 5])

# Klasik Döngü ile

ab = []

for index in i:
    if index < 3:
        ab.append(index)

print(ab)

# numpy ile

print(i[i<3])
print(i[ i != 3]) # gibi işlemler de yapılabilir.

print(i/2, i*3, i ** 4)

print(np.subtract(i, 1), np.add(i, 1), np.mean(i), np.sum(i), np.max(i), np.var(i)) # gibi işlemler de gerçekleştirilebilir.
