import random

def guess_number(name='Ayush'):
    user_number = int(input(f"{name}, enter the number: "))
    actual_number = random.randint(1, 100)
    if user_number <=0 and user_number > 100:
        print(f"{name},please enter values from 1 to 100")
    else:
     while True:
        if user_number == actual_number:
            print(f"🎉 {name} you guessed the correct number")
            break
        elif user_number<actual_number:
            print(f"😲 {name} Keep on trying you are close")
        else:
            print(f"🤦‍ {name}, you are far from the actual number")

        user_number = int(input("Enter again: "))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalised game experience")
    parser.add_argument("-n","--name",metavar="name",required=True,
                         help="The name of the person who is playing the game")
    args=parser.parse_args()
    guess_number(args.name)
    # guess_my_number()

