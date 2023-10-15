
#? 100'e kadar olan sayıların toplamı

toplam = 0
i = 0
while i < 101:
    toplam += i
    i +=1
print(toplam) 


print('*' * 70)


#? Kullanıcının girdiği değere kadar olan çift sayıların toplamı

cift_toplam = 0

kullanici_deger = int(input('0 - 1000: '))
x = 0 
while x < (kullanici_deger + 1):
    if x % 2 == 0:
        cift_toplam += x
    x += 1
print(cift_toplam)

print('*' * 70)

#? FizzBuzz Oyunu

y = 0
while y < 100:
    if (y % 5 == 0) and (y % 3 == 0):
        print("FizzBuzz")
    elif y % 3 == 0:
        print ("Fizz")
    elif y % 5 == 0:
        print("Buzz")
    else:
        print(y)
    y +=1


