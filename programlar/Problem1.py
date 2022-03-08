# Problem 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını
# bulmaya çalışın.

# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse
# bu sayıya "mükemmel sayı" denir. Örnek olarak,
# 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)


print("Sayınızın mükemmel olup olmadığını kontrol etmek için girin\nçıkmak için 'q' ya basın\n")

while(True):
    i=1
    toplam=0
    i=1
    sayi = input("\nsayi girin: ")
    if(sayi == "q"):
        break
    while(i <= ( int(sayi)) / 2):
        if((int(sayi) % i) == 0):
            toplam += i
        i += 1
    
    if(toplam == int(sayi)):
        print("sayınız mükemmel sayıdır.")
    else:
        print("sayınız mükemmel değildir.")
    
    
else:
    print("çıkış yaptınız....")