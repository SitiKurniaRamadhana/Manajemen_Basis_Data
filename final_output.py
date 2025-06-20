import json

with open('Final_SitiKurniaRamadhana.json') as f:
    data = json.load(f)

mhs = data["mahasiswa"]
print("Data Mahasiswa:")
print(f"Nama    : {mhs['nama']}")
print(f"Nim     : {mhs['nim']}")
print(f"Kelas   : {mhs['kelas']}")
print(f"Angkatan: {mhs['angkatan']}")