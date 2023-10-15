
#? Girilen notlar arasında en yüksek notu seçme
notlar = input('Notlar: ').split()
i = 0
while i < len(notlar):
    notlar[i] = int(notlar[i])
    i += 1

max_deger = 0
skor = 0

while skor < len(notlar):
        if notlar[skor] > max_deger:
            max_deger = notlar[skor]
        skor += 1

print(max_deger)
