import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 11
if difficulty == 'hard':
    attempts = 6
answer = random.randint(1,100)
guess = 0
while guess != answer:
    attempts -= 1
    print(f"you have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The answer was {answer}.")
        break
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    if guess > answer:
        print("Too high")
    if guess < answer:
        print("Too low")