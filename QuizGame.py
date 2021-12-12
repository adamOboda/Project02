print("Hello")

playing = input("Do u want to play game? ")
if playing.lower() != "yes":
    quit()
print("Let's play")
score = 0

answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect, Try again")

answer = input("Which IPhone do you have? ")
if answer.lower() == "iphone x":
    print("Correct")
    score += 1
else:
    print("Incorrect, Try again")

answer = input("Which BMW do you have? ")
if answer.lower() == "e39":
    print("Correct")
    score += 1
else:
    print("Incorrect, Try again")

print("You have " + str(score) + " points")