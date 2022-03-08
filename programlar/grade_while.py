# [grade_while.py]
bExit=False
while not bExit:
 command=input("Enter a score(""q"" to exit):")
 if command=="q":
     bExit=True
 else:
     score=float(command)
     if 85 <=score <=100:
         print("A")
     elif 70 <=score < 85:
         print("B")
     elif 50 <=score < 70:
         print("C")
     elif 0 <=score < 50:
         print("D")
     else:
         print("Invalid score entered")
         