#Problem 3
#1'den 10'kadar olan sayılarla ekrana
#çarpım tablosu bastırmaya çalışın.

#İpucu: İç içe 2 tane for döngüsü kullanın.
#Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.

for i in range(1,11):
    for j in range(1,11):
        print("%d x %d : %d\n"%(i,j,i*j))