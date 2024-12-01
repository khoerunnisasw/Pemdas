data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 920,
            'kedelai': 480
        }
    }
}


print("\nSoal No. 1")
for lokasi, detail in data_panen.items():
    print(f"{lokasi}: {detail}")

print("\nSoal No. 2")
jumlah_jagung_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"\nJumlah hasil panen jagung di lokasi2: {jumlah_jagung_lokasi2}")

print("\nSoal No. 3")
nama_lokasi3 = data_panen["lokasi3"]["nama_lokasi"]
print(f"\nNama lokasi 3: {nama_lokasi3}")

print("\nSoal No. 4 & 5")
jumlah_padi = []
jumlah_kedelai = []

for lokasi, detail in data_panen.items():
    jumlah_padi.append(detail['hasil_panen']['padi'])
    jumlah_kedelai.append(detail['hasil_panen']['kedelai'])

print("Jumlah hasil panen padi setiap lokasi:", jumlah_padi)
print("Jumlah hasil panen kedelai setiap lokasi:", jumlah_kedelai)

print("\nSoal No. 6")
for lokasi, hasil in data_panen.items():
    if hasil["hasil_panen"]["padi"] > 1300 or hasil["hasil_panen"]["jagung"] > 800:
        print(f"{lokasi} memerlukan perhatian khusus.")
    else:
        print(f"{lokasi} dalam kondisi baik.")
<<<<<<< HEAD
=======

print("Sudah di branch baru")
>>>>>>> Baru
