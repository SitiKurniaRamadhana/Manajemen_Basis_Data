import json

# Baca file JSON
with open('key_value_db.json', 'r') as file:
    data = json.load(file)

# Tampilkan setiap data mahasiswa
print("📄 Daftar Data Mahasiswa:")
print("-----------------------------")
for i, mhs in enumerate(data, start=1):
    print(f"Mahasiswa {i}:")
    print(f"  Nama          : {mhs['nama']}")
    print(f"  Tanggal Lahir : {mhs['tanggal_lahir']}")
    print(f"  Alamat        : {mhs['alamat']}")
    print(f"  Email         : {mhs['email']}")
    print("-----------------------------")