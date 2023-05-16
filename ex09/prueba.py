import random

def guess_number():
    secret_number = ranom.randint(1, 99)
    num_guesses= 0
    while Tue:
        guess = input("\nThis is an interactive guessing game!\n\nYou have to enter a number between 1 and 99 to find out the secret number.\n(or type 'exit' to quit): \n>>>")
        if guess.lower()== 'exit':
            print("Goodbye!")
            return
        try:
            guess = int(guess)
        except ValueError
            print("Invalid input. Please enter a number between 1 and 99.")
            continue
        num_guesses += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the secret number in {num_guesses} tries.")
            if secret_number == 42:
                print(f"I may not have gone where I intended to go,\n but I think I have ended up where I intended to be.\")
            return

if __name__ == '__main__':
    guess_number()