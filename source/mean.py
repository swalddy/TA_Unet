import numpy as np
import cv2
import os

# Ini adalah list dari semua path gambar latihan Anda
image_paths = [os.path.join('C:\\Users\\oswal\\Documents\\Kuliah\\Semester 7\\Pra-TA\\Baru\\GID\\GID\\taset\\raw_new', file) for file in os.listdir('C:\\Users\\oswal\\Documents\\Kuliah\\Semester 7\\Pra-TA\\Baru\\GID\\GID\\taset\\raw_new')]

# Inisialisasi list untuk menyimpan mean dari setiap gambar
means = []

# Loop melalui semua gambar untuk menghitung mean
for image_path in image_paths:
    # Baca gambar menggunakan OpenCV
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Jika gambar adalah BGR, konversi ke RGB
    
    # Hitung mean dari gambar dan tambahkan ke list means
    means.append(np.mean(image, axis=(0, 1)))  # Axis (0, 1) artinya kita menghitung mean melintasi lebar dan tinggi gambar

# Hitung mean keseluruhan dari seluruh dataset
train_mean = np.mean(means, axis=0)

print(f"Mean keseluruhan dataset adalah: {train_mean}")
