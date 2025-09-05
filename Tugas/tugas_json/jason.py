import json

# materi 11 kelas A dengan json

# tambahkan module `json`` dengan `import`
print("Materi 11 - JASON IS THE BEST")
print("-------- RED JSON  -----------")

file_path_json = r"C:\Jamal new\New folder\materi.10\tugas_json\materi.json"
# siapkan data  kosong 
# 
# 1. Baca seluruh data
with open(file_path_json, "r") as file_materi:
  # csv.reader() -> membaca isi file csv
  data_materi = json.load(file_materi)
   #akses data json dengan 'key' nya 
    
  print(f"judul berkas: {data_materi['title']}")
  print(f"total kelas A: {data_materi['total']}")
  print(f"status_santri: {data_materi['status_santri']}")
  print(f"status_kelulusan: {data_materi['status_santri']}")
  for pelajaran in data_materi ['pelajaran']:
    print(f"---> {pelajaran}")

  print("| nama | surah['no'] | surah['nama'] | surah['turun'] | surah['ayat]")
  for surah in data_materi['surah'] :
    print (f"| { surah['no']} | { surah['nama']} | {surah['turun']} | {surah['ayat']}")