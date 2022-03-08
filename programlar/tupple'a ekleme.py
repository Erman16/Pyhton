
# tupple vb. şeye bişey eklemek için kolay yol

e = ()
x = 9
e += (x,)  #bunu yapıyoruz
print(e)

# kolay örnek

e = ()
a=0
x = 0
while (a < 5):
    x = a+2
    e += (x,)
    a += 1
print(e)

#--------- örnek ----------------------------------

a = 0
s = ()
while (a < 5):
    s += (int(input("%d.sayiyi gir"%(a+1))),)
    a += 1
print(s)
