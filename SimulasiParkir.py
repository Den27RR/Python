import numpy as np
import threading
import time

lambd = 2
scale = 1 / lambd
pelanggan = int(input("Masukkan jumlah pelanggan : "))
ruang_tunggu = list()
datang = np.random.exponential(scale=0.5, size=pelanggan)
# print("Interval Kedatangan\n",datang)
exp = np.cumsum(datang)
layanan = np.random.exponential(scale=0.5, size=pelanggan)
# print("\nInterval Pelayanan\n", layanan)
i = 0
waktu = [0] * pelanggan  # Buat list waktu yang sesuai
waktu_awal = time.time()

print("============================================================================")
print("| Keterangan | Waktu Interval | Orang di Ruang Tunggu |        Waktu       |")
print("============================================================================")

# Variabel untuk mengontrol penghentian
banyak_pelanggan = 0
batasan_pelanggan = pelanggan

def kedatangan():
    global banyak_pelanggan
    for j in range(len(datang)):
        time.sleep(datang[j] * 60)
        # time.sleep(datang[j])
        ruang_tunggu.append(1)
        banyak_pelanggan += 1
        print(f"| Masuk      | {datang[j]:.8f}     |            {len(ruang_tunggu)}          | {((time.time()-waktu_awal)/60):.8f} Menit   |")

        if banyak_pelanggan >= batasan_pelanggan:
            break

def pelayanan():
    global i
    while i < len(layanan):
        if ruang_tunggu:
            time.sleep(layanan[i] * 60)
            # time.sleep(layanan[i])
            ruang_tunggu.pop()
            waktu[i] = exp[i] + layanan[i]

            print(f"| Dilayani   | {layanan[i]:.8f}     |            {len(ruang_tunggu)}          | {((time.time()-waktu_awal)/60):.8f} Menit   |")
            i += 1

# Buat dua thread terpisah untuk kedatangan dan pelayanan
thread_kedatangan = threading.Thread(target=kedatangan)
thread_pelayanan = threading.Thread(target=pelayanan)

# Jalankan kedua thread secara bersamaan
thread_kedatangan.start()
thread_pelayanan.start()

