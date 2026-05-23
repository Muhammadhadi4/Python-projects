import random
target = random.randint(1, 10)
i = 1

while i > 0:
    guess = int(input("Guess a number (1-10): "))
    
    if guess == target:
        print("You found it! ")
        break
    elif guess < target:
        print("Too low!")
        i = i + 1
    elif guess > target:
        print("Too high!")
        i = i + 1

print("Total tries:", i)
