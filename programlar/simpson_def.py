#[simpson_lambda]
#integral of x^2 between 0 and 10

def simpson(f,a,b,n):
    d=float(b-a)/n
    sq=lambda x: x**3-x**2+3*x+5
    #f(a)
    fa=f(a)
    #f(b)
    fb=f(b)
    #sum f(a+id)
    s1=0
    i=1
    while i<=n-1:
        s1+=f(a+i*d)
        i+=1
    #sum f(a+(i+0.5)d
    s2=0
    i=0
    while i<=n-1:
        s2+=f(a+(i+0.5)*d)
        i+=1
    #area
    s=(d/6)*(fa+2*s1+4*s2+fb)
    return s

#main
f=lambda x:x*x
a=0
b=10
n=1000
print("The integral is equal to ", simpson(lambda x: x*x, 0, 10, 10000))
        