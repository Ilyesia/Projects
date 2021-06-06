import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: #this loops if the guess does not equal the random integer
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number: #This if loop allows return of information if you're above or below the random integer
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")

    print(f"You guessed the number {random_number} correctly!")
# if your guess is correct the first try this if loop isn't initated 

def computer_guess(x):
    lower_bound = 1
    higher_bound = x
    feedback = ""
    while feedback != "c":
        if lower_bound != higher_bound:
            guess = random.randint(lower_bound, higher_bound) #random.randint will error if low and high are the same number.
        else:
            guess = lower_bound #this could also be higher_bound but they're the same number so it doesn't matter which one is used
        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            higher_bound = guess - 1
        elif feedback == "l":
            lower_bound = guess + 1
        
    print(f"The computer has guessed your number {guess} correctly.")

computer_guess(50) #Make sure to set (x) when defining something else and not like an idiot who forgot guess != computer_guess
guess(25) #this sets the variable (x)

