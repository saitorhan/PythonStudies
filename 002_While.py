x = input("Tekrar sayısını giriniz")
x = int(x)

y = -5

while y < x :
    if y == 0:
        y = y + 1
        continue

    print(x / y)
    y = y + 1


print("İkinci while")

y = 0

while y < x:
    if y % 2 == 0:
        break
    print(y)
    y = y +1
else:
    print("ikinci while bitti")


print("Döngü sona erdi")

# saitorhan.com
