sayi1 = input("İlk sayıyı giriniz")

islem = input("""Yapmak istediğiniz işlemi seçiniz:
+ : Toplama
- : Çıkarma
* : Çarpma
/ : Bölme
% : Mod Alma
f : Faktoriyel Alma
""")
if islem != "f":
    sayi2 = input("İkinci sayıyı giriniz")

sonuc = 0;

if islem == "+":
    sonuc = float(sayi1) + float(sayi2)
elif islem == "-":
    sonuc = float(sayi1) - float(sayi2)
elif islem == "*":
    sonuc = float(sayi1) * float(sayi2)
elif islem == "/":
    sonuc = float(sayi1) / float(sayi2)
elif islem == "%":
    sonuc = float(sayi1) % float(sayi2)
elif islem == "f":
    sonuc = 1
    for i in range(1, int(sayi1) + 1):
        sonuc = sonuc * i

print(islem, "İşleminin Sonucu =", sonuc)
