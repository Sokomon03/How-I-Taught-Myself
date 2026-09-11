import random

print("Welcome to my first python project! The guessing game!")

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    
    attempts = attempts + 1
    
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"You got it in {attempts} tries")
        
    
    
