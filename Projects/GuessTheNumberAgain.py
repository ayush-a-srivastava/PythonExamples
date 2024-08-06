import random

def play_mode(no_of_attempts):
    guess_number = random.randint(1, 100)
    while no_of_attempts != 0:
        user_number = int(input("Enter any number (between 1-100) : "))
        if user_number < guess_number:
            print("You guessed too small!")
        elif user_number > guess_number:
            print("You guessed too high!")
        elif user_number == guess_number:
            print("Congrats!! You have guessed the number")
            break
        no_of_attempts = no_of_attempts - 1
        print(f"You have {no_of_attempts} attempts left. ")
    else:
        print("Sorry, you have used all your attempts.")
    print("The guessed number was: ", guess_number)


mode = input("Enter the difficulty level (easy/hard): ")
if mode == "easy":
    play_mode(10)
elif mode == "hard":
    play_mode(5)
else:
    print("Please enter the correct mode.")
