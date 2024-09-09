print("Wecome to my computer quiz!")

playing = input("Do yo want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")

score = 0

answer= input("What does CUP stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is 5 multiplied by 6? ")
if answer == "30":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the square root of 64? ")
if answer == "8":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the boiling point of water in Celsius? ")
if answer == "100":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the capital of Japan? ")
if answer.lower() == "tokyo":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the result of 9 divided by 3? ")
if answer == "3":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the freezing point of water in Celsius? ")
if answer == "0":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("you got " +str(score)+" questions correct!")
print("you got "+ str((score/10)*100)+" %")






