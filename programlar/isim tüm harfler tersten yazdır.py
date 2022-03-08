#kullanıcıdan isim soyisim alıp tersten
#tüm harfleri tersten yazdır.
#örn: Erman Yalçın --> nıçlaY namrE

name = input("please enter your name: ")
surname = input("please enter your surname: ")

print(surname[::-1],name[::-1])
