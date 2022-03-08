
import math
e = 2.718281

while(True):
    print("---Electric field and potential calculator program---\n")
    cubuk = float(input("Please enter the length of the rod (in meters): "))
    x0 = float(input("Please enter your x0 value (in meters): "))
    print("--------------------------------------------------\nWhile entering the value Q Use x.10^n \nThat means, for 20.10^-6 enter x = 20 , n = -6\n")
    q = float(input("Please enter x value: "))
    n = float(input("Please enter n value: "))
    k = 9 * (10**9)
    lamda = q* (10**n) / cubuk
    E = k * lamda * ( (1/(x0-cubuk)) - (1/x0) )
    V = k * lamda * ( math.log(x0,e) - math.log(x0-cubuk,e) )
    print("Electric field: %d\nElectric potential: %d\n"%(E,V))
    a = int(input("Press 0 to exit 1 to continue: "))
    if(a == 0):
        break
print("Closing...")