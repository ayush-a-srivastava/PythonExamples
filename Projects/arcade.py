import sys
from GuessNumber import guess_number
from RockPaperScissors import RockPaperScissors

def play_game(name="Ayush"):
    welcome_back=False

    while True:
        if welcome_back == True:
           print(f"{name} Welcome back to the Arcade menu. 🤖")

        playerChoice = input("Enter \n1 for Rock Paper Scissor game \n2 for Guess the Number game \nq for exit(): \n ")
        if playerChoice not in ["1","2","q"]:
            print(f"{name} Please enter 1,2 or q")
            return play_game(name)
        welcome_back = True
        if playerChoice == '1':
            RockPaperScissors(name)
        elif playerChoice == '2':
            guess_number(name)
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalised game experience")
    parser.add_argument("-n","--name",metavar="name",required=True,
                         help="The name of the person who is playing the game")
    args=parser.parse_args()
    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    play_game(args.name)