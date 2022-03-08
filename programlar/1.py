a = int(input("please enter a:"))
b = int(input("please enter b:"))
c = int(input("please enter c:"))
x = int(input("please enter x:"))

def quadratic(a,b,c,x):
    delta = b**2-(4*a*c)
    #answer of fx:
    fx=a*(x**2)+b*x+c
    print("fx={}".format(fx))
    #
    #answer of delta and finding roots:
    if delta<0:
        print("there is no solution")
    elif delta==0:
        print("there is one root")
        x1 = (-b+delta**(1/2))/(2*a)
        print("root:{}".format(x1))
    else:
        print("there is two root")
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        print("root 1 is:{}".format(x1))
        print("root 2 is:{}".format(x2))       

quadratic(a,b,c,x)


        