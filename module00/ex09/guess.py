import sys
import random

def guess():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print("")

    attempts = 0
    secret_number = random.randint(1, 99)

    while True:
        print("What's your guess between 1 and 99?")
        user_input = input(">>")
        if user_input == "exit":
            sys.exit(0)

        elif not user_input.isdigit():
            print("That's not a number.")

        else:
            guess = int(user_input)
            if guess < 1 or guess > 99:
                print("That's not a number between 1 and 99.")
            else:
                attempts += 1
                if guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print("Congratulations, you've got it!")
                    print(f"You won in {attempts} attempts.")
                    break

def main():
    if len(sys.argv) != 1:
        print(f"Usage: python {sys.argv[0]}")
        sys.exit(1)
    else:
        guess()

if __name__ == "__main__":
    main()