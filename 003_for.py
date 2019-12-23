sehirler = ["Kayseri", "Batman", "İstanbul","Ankara"]

cumle = "Bu cümle for döngüsü için yazılmıştır"

for sehir in sehirler:
    print(sehir)

else:
    print("Şehirler ekrana yazıldı")

for harf in cumle:
    print(harf)

else:
    print("Harfler ekrana yazıldı")

for sayi in range(10):
    print(sayi)
print("range aralıklı")

for sayi in range(10,20):
    print(sayi)

print("range artılımlı")

for sayi in range(10,50, 3):
    print(sayi)