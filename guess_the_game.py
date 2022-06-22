import random

def guess(x):
    random_nm = random.randint(1,x)
    guess = 0
    while guess != random_nm:
        guess =int( input(f"Guess a number between 1 and {x}"))
        if guess < random_nm:
            print("Your guess is too low")
        elif guess > random_nm:
            print("Your guess is too high")
    print("You have guessed the correct number.") 

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess =  low    
        feedback = input(f"Is {guess} too high(H) , too low(L) or correct(C) ?").lower()
        if feedback == 'h':
           high =  guess - 1
        if feedback == 'l':
            low = guess + 1   
    print(f"Yay! The computer guessed your number,{guess}, correctly!")
        
computer_guess(20)