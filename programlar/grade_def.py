# [grade_def.py]
def grade(score):
    if 85 <=score <=100:
        return "A"
    elif 70 <=score < 85:
        return "B"
    elif 50 <=score < 70:
        return "C"
    elif 0 <=score < 50:
        return "D"
    else:
        return None
# main
bExit=False
while not bExit:
    command=input("Enter a score(q to exit):")
    if command=="q":
        bExit=True
    else:
        score=float(command)
        g=grade(score)
        if g==None:
            print("Invalid score entered")
        else:
            print(g)   