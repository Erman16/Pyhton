#kullanıcıdan bir rakam al diyelim n olsun
#ve bu rakamı n+nn+nnn şeklinde hesaplayıp
#ekrana yazdır.
#örn: n=5, 5+55+555=615 --> ekrana 615 yazdır.

n = int(input("please enter numeral: "))

n2 = n*10 + n
n3 = n*100 + n*10 + n
sonuc = n+n2+n3
print(sonuc)

#alternatif çözüm:

a = int(input("please enter numeral: "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)