import random

names = ['ayush', 'sneha', 'akash', 'akshat', 'vishal']
random_name = random.choice(names)
print(f"The name is {random_name}")
display_name = []
for _ in random_name:
    display_name += '-'
print(display_name)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess the character: ")

    if guess in display_name:
        print(f'You already guessed {guess}')

    for position in range(len(random_name)):
        if random_name[position] == guess:
            display_name[position] = guess

    if guess not in random_name:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print("You lose !")
    print(display_name)

    if '-' not in display_name:
        end_of_game = True
        print("You win! ")

