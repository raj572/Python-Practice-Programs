import random

print('''\t\t----------------------------------------------------------
        \t\t------------WELCOME TO ELEMENTAL CLASH GAME------------------
          ------------------------------------------------------------------''')

while True:
    user_score = 0
    computer_score = 0

    while True:
        elemental_actions = ['Fire', 'Water', 'Earth']
        computer_action = random.choice(elemental_actions)
        user_action = input('Enter your choice (Fire, Water, or Earth): ')
        print('Your Choice -->', user_action)
        print('Computer Choice -->', computer_action)

        if user_action not in elemental_actions:
            print('Please enter a valid element name!')
        else:
            if user_action == computer_action:
                print("It's a tie!")
            elif (user_action == 'Fire' and computer_action == 'Earth') or \
                 (user_action == 'Earth' and computer_action == 'Water') or \
                 (user_action == 'Water' and computer_action == 'Fire'):
                print('Congrats! You Won!')
                user_score += 5
                computer_score -= 1
            else:
                print('Oops! You lose :(')
                user_score -= 1
                computer_score += 5
                print('Point 1 is deducted as you lose')

            print(f'Your current score is {user_score}')
            print(f'Computer current score is {computer_score}')

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    if user_score > computer_score:
        print('Congrats!! You won this game :)')
    elif user_score < computer_score:
        print('Oops! You lose!! Better luck next time :(')
    else:
        print("It's a tie.")

    print(f'Your total score is {user_score}')
    print(f'Computer score is {computer_score}')

    exit_game = input("Do you want to exit the game? (yes/no): ").lower()
    if exit_game == "yes":
        break
