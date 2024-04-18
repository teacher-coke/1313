import random
counter = 0
f = random.randint(1, 100)
for i in range(100):
    j = int(input("Enter an integer between 1 and 100: "))
    if f < j:
        print("The number is smaller than", j)
        counter += 1
    elif f > j:
        print("The number is bigger that", j)
        counter += 1
    elif f == j:
        print("You got it! You took", counter, "tries")
        break