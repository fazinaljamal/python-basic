import requests

url = "https://api.aladhan.com/v1/timingsByCity?city=Jakarta&country=Indonesia&method=20"

response = requests.get(url)
print("Status code:", response.status_code)   # harusnya 200 kalau sukses

data_json = response.json()
print("Data keys:", data_json.keys())         # cek struktur JSON

tanggal = data_json['data']['date']['readable']
jadwal = data_json['data']['timings']

print("Tanggal:", tanggal)
for sholat, waktu in jadwal.items():
    print(f"{sholat:10} : {waktu}")
