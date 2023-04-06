import random

if __name__ == "__main__":
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
    num = random.randint(1, 99)
    attempts = 0
    while True:
        attempts += 1
        line = input("What's your guess between 1 and 99\n")
        if line == 'exit':
            print("Goodbye!")
            break
        try:
            inp_num = int(line)
            if inp_num > num:
                print("Too high!")
            elif inp_num < num:
                print("Too low!")
            else:
                if (num == 42):
                    print(
                        """The answer to the ultimate question of life, the universe and everything is 42.""")
                if (attempts == 1):
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in {} attempts!".format(attempts))
                break
        except ValueError:
            print("That's not a number.")
