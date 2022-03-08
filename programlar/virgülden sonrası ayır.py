#kullanıcıdan 5 sayı girmesini ama sayıların
#arasına virgül koyarak yazmasını isteyin
#sonra bu sayıları list ve tuple'a atıp ikisini de ekrana bastırın
#ipucu: (.blabla) şeklindeki formatları kullan.

sayilar = input("please enter: ")
liste = sayilar.split(",")
tuple_ = tuple(liste)

print(liste,"\n",tuple_)
