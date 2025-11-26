#tuple#
# Menyimpan data mahasiswa dalam bentuk tuple
mahasiswa = ("Aulia", 19, "Teknik Informatika")

# Menampilkan seluruh data
print("Data Mahasiswa:")
print("Nama :", mahasiswa[0])
print("Usia :", mahasiswa[1])
print("Jurusan :", mahasiswa[2])

# Tuple tidak bisa diubah, tapi kita bisa menyalin datanya ke list jika ingin memodifikasi
# Contoh:
mahasiswa_list = list(mahasiswa)
mahasiswa_list[1] = 20  # Mengubah usia
mahasiswa_baru = tuple(mahasiswa_list)

print("\nData Mahasiswa Setelah Diubah (versi tuple baru):")
print(mahasiswa_baru)


#list

# Membuat list awal berisi beberapa item
daftar_belanja = ["Telur", "Gula", "Minyak"]

print("Daftar Belanja Awal:", daftar_belanja)

# Menambah item baru
daftar_belanja.append("Beras")
print("Setelah menambah item:", daftar_belanja)

# Mengubah item (misal 'Gula' diganti 'Gula Merah')
daftar_belanja[1] = "Gula Merah"
print("Setelah mengubah item:", daftar_belanja)

# Menghapus item
daftar_belanja.remove("Minyak")
print("Setelah menghapus 'Minyak':", daftar_belanja)

# Menampilkan daftar belanja satu per satu
print("\nDaftar Belanja Terbaru:")
for item in daftar_belanja:
    print("-", item)
