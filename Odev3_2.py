kullanici_kilo = input('Sinifin Kilolari: ').split()
# kullanici_kilo = list(input('Sinifin Kilolari: '))


#? kendisinin int haline eşitliyoruz
i = 0
while i < len(kullanici_kilo):
    kullanici_kilo[i] = int(kullanici_kilo[i])
    print(kullanici_kilo)
    i += 1

toplam_kilo = 0
kilo = 0
while kilo < len(kullanici_kilo):
    toplam_kilo += kullanici_kilo[kilo]
    kilo += 1
print(f'Toplam kilo: {toplam_kilo}')

ogrenci_sayisi = len(kullanici_kilo)
print('Öğrenci Sayisi: {}'.format(ogrenci_sayisi))

ortalama = toplam_kilo / ogrenci_sayisi
print(ortalama)

