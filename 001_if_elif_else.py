# input ile kullanıcıdan değer alma ve koşullu işleme

yas = int(input("Yaşınızı Giriniz"))

if yas < 18:
    print("Yaşınız sisteme kayıt için uygun değildir.")
    print("Lütfen çıkış işlemi için \"ENTER\" tuşuna basınız")

elif yas >= 18 and yas < 25:
    print("Sisteme geçici kaydınız alındı")
    if yas == 21:
        print("Tebrikler!")
    else:
        print("Gene tebrikler")

elif yas >= 25 and yas < 40:
    print("Sisteme kaydınız onay beklemektedir")

else:
    print("Hastane Yönetim Sisteminde hesabınız açılmıştır")
    print("Email hesabınızı kontrol ediniz")

print("if ifadesi şartı doğru olduğunda çalışır")

# and ifadesi ve demektir. doğru olması için ikisinde doğru olması lazım
# or ifadesi de veya demektir ve şartlardan herhangi biri doğru ise şart sağlanmış olur
# > , <, == , >= , <=,  !=