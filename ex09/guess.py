import random
import sys

def guess_number(): 
    
    secret_number = ramdon.randint(1, 99)
    num_guesses = 0
    print("\n This is an interactive guessing game!")
    print("\nYou have to enter a number between 1 and 99 out the secret number.\nType 'exit' to end the game.\nGood look!!")
    while True:
        guess = input("\nWhat's your guess between 1 and 99?\n>>>")
        if guess.lower() == 'exit':
            print("\nGoodbye!!\nSee you later, alligator!!\n")
            return
        try:
            guess = int(guess)
        except ValueError:
            print("\nInvalid Input. Please enter a number between 1 and 99.\n")
            continue
        if guess < 1 or guess > 99:
            print("\nNumber out of range.\nPlease enter a number between 1 and 99.\n")
            continue
        num_guesses += 1
        if guess < secret_number:
            print("\nToo low!")
        elif guess > secret_number:
            print("too high!!")
        else :
            if secret_number == 42:
                print(f"\n   I may not have gone where I intended to go,\nbut I think I have ended up where I intended to be.\n\nCongratulations! You guessed the secret number in {num_guesses} tries.\n")
            else:
                print(f"Congratulations! You guessed the secret number in {num_guesses} tries.")
            return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("\nError: Too many arguments.\n\nUsage: < python3 my_program.py >\n")
    else:
        guess_number()
