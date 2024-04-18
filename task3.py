import random
user = int(input("Rock(1), paper(2), or scissors(3)? "))
computer = random.randint(1, 3)
if computer == 1:
    if user == 2:
        print("The computer chose rock. You won!")
    elif user == 1:
        print("The computer chose rock. Tie!")
    elif user == 3:
        print("The computer chose rock. You lost!")
elif computer == 2:
    if user == 2:
        print("The computer chose paper. Tie!")
    elif user == 1:
        print("The computer chose paper. You lost!")
    elif user == 3:
        print("The computer chose paper. You won!")
elif computer == 3:
    if user == 2:
        print("The computer chose scissors. You lost!")
    elif user == 1:
        print("The computer chose scissors. You won!")
    elif user == 3:
        print("The computer chose scissors. Tie!")
