import csv

# materi 11

# tambahkan module `csv`` dengan `import`
print("Materi 11 - File Handling Part 2")
print("-------- UPDATE CSV -----------")
# baca isi file -> ekstrak data -> buat data baru
# -> tulis ulang semua isi barisnya dengan mode 'w'
file_path_csv = r"\Jamal new\New folder\materi.10\csv_jamal\jajan_csv\jajan 10 a.csv"
# siapkan data jaja kosong 
# untuk menampung data dari csv ke list
data_jajan = []
# 1. Baca seluruh data
with open(file_path_csv, "r") as file_jajan:
  # csv.reader() -> membaca isi file csv
  isi_table_jajan = csv.reader(file_jajan)
  # esktrak semua data dengan for loop
  for item_jajan in isi_table_jajan:
    # print(item_jajan)
    # tambah item ke list data jajan
    data_jajan.append(item_jajan)

# 2. mengubah atau membuat data baru
for item in data_jajan:
  print(f"Proses Item No => {item[0]}")
  print(item)
  # jika kolom nama (index 1) adalah "nama"
  if item[1] == "Thufail":
    # ganti kolom uang (index 2) dengan nilai baru
    uang_jajan_baru = 15000
    item[2] = uang_jajan_baru
    print(f"Data ditemukan, ganti uang jajan {uang_jajan_baru}")
  print('-----Loop End------')  

# hapus data di list index 2
del data_jajan[2]
print(f"DATA JAJAN TERKINI: {data_jajan}")
# 4. tulis ulang data dengan mode 'w' -> write
with open(file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    # .writerows() -> tulis sekali banyak
    writer.writerows(data_jajan)
    
