#[simpson_lambda]
#integral of x^2 between 0 and 10
a=0
b=10
n=10000
d=float(b-a)/n
sq=lambda x: x*x
#f(a)
fa=sq(a)
#f(b)
fb=sq(b)
#sum f(a+id)
s1=0
i=1
while i<=n-1:
    s1+=sq(a+i*d)
    i+=1
#sum f(a+(i+0.5)d
s2=0
i=0
while i<=n-1:
        s2+=sq(a+(i+0.5)*d)
        i+=1
#area
s=(d/6)*(fa+2*s1+4*s2+fb)
print('the integral is equal to',s)
        