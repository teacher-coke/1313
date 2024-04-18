import random
guess = int(input("Heads(1) or tails(2)? "))
flip = random.randint(1, 2)
if guess == flip:
    print("You got it!")
else:
    print("Nope!")

