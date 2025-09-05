# materi 10 a
import csv

file_path = r"\Jamal new\New folder\materi.10\jajan 10 a.csv"
with open(file_path, "r") as file_pesan:
  isi_pesan = file_pesan.read()
  print (f"isi pesan ====> {isi_pesan}")

print("open vile csv")


# data yang mau dtambahkan

jajan_baru = [6,"jamal",10000]
print(f"jajan baru: {jajan_baru}")

# menulis data baru ke csv

with open(file_path,"a",newline="") as file_jajan:
  writer = csv.writer(file_jajan)
  writer.writerow(jajan_baru)
  

