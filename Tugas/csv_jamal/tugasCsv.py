import csv

# Lokasi file CSV
file_path = r"C:\Python Basic\Tugas\csv_jamal\tugas.csv"

# --- Baca isi file ---
with open(file_path, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    data = list(reader)

print("=== Data Pengeluaran Awal ===")
for row in data:
    print(row)

# --- Tambahkan data baru ---
data.append(["2025-08-26", "Bakso", "Makan", "15000"])
data.append(["2025-08-27", "GoRide", "Transportasi", "12000"])

print("\n=== Data Setelah Ditambah ===")
for row in data:
    print(row)

# --- Simpan lagi ke file CSV ---
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("\nData berhasil ditambah dan disimpan ke:", file_path)
