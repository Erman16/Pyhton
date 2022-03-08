i = 0
s = 0
n = 10
ort = float
a = []
passes = []
while(i < n):  
    a.append(int(input("Please enter your %d note: "%(i+1))))
    i+=1
i=0
while(i < n):  
    s = s + a[i]
    i+=1
i=0
ort = s/n
print("Notes:",a,"\nAverage:",ort)
while(i < n):  
    if(a[i] > ort):
        passes.append(a[i])
    i+=1
print("Pased ones:",passes)
