computer_choice = 'scissor'

user_choice = input('Do you want - rock, paper or scissor?\n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissor':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose: (Computer win :D)')