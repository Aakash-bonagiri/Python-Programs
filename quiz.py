print(" Welcome to the quiz!")

choice = input("Do you wan to play? (yes/no)")
score = 0
if choice.lower() != "yes":
    quit()

answer = input("What does CPU stand for? ")
if answer.lower()  == "central processing unit":
    print("Correct!")
    score+= 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower()  == "graphics processing unit":
    print("Correct!")
    score+= 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower()  == "random access memory":
    print("Correct!")
    score+= 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower()  == "power supply":
    print("Correct!")
    score+= 1
else:
    print("Incorrect!")

print("You have scored " + str(score))
print("You have scored "+ str((score/4)*100)+ "%.")