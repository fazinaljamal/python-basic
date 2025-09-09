import requests

# Arab
url_ar = "https://api.alquran.cloud/v1/ayah/2:255/ar.alafasy"
resp_ar = requests.get(url_ar).json()
ayat_ar = resp_ar["data"]["text"]

# Inggris
url_en = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"
resp_en = requests.get(url_en).json()
ayat_en = resp_en["data"]["text"]

print("Al-Baqarah [255] - Ayat Kursi\n")
print("--- Teks Arab ---")
print(ayat_ar)

print("\n--- Translation (English) ---")
print(ayat_en)
