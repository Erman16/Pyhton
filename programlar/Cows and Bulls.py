#Cows and Bulls
import random

cows = 0
bulls = 0
control = 0
number = str(random.randint(1000,9999))
def cab(cows,bulls,number):
    guess = input("Please enter 4-digit number.")
    for i in range(4):
        if(number[i] == guess[i]):
            cows += 1
    if(guess < number):
        print("enter bigger number")
    elif(guess > number):
        print("enter lower number")
    bulls = 4-cows
    print("cows: %d , bulls: %d"%(cows,bulls))
    return cows
while(control != 4):
    control = cab(cows,bulls,number)
print("Well done!!!")
