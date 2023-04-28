import random
a = 'y'

def game_win(comp, you):
    if comp == you:
        return None
    elif comp == 'rock':
        if you == 'scissor':
            return False
        elif you == 'paper':
            return True
    elif comp == 'scissor':
        if you == 'paper':
            return False
        elif you == 'rock':
            return True
    elif comp == 'paper':
        if you == 'rock':
            return False
        elif you == 'scissor':
            return True
    else:
        return 'Not a valid input!'
while a == 'y' or a == 'ye' or a == 'yes':
    print('Computer is doing its turn...')
    input_of_user = input('Your turn, what do you choose(type rock,scissor or paper)\n')
    choice_of_comp = random.randint(1,3)
    if choice_of_comp == 1:
        real_choice_of_computer = 'rock'
    elif choice_of_comp == 2:
        real_choice_of_computer = 'paper'
    else:
        real_choice_of_computer = 'scissor'
    input_of_user = input_of_user.lower()
    a = game_win(real_choice_of_computer, input_of_user)
    if a is None:
        print(f'The match is a tie!! as computer chose {real_choice_of_computer} and ', end='')
        print(f'you chose {input_of_user}')
    elif a:
        print(f'You won!!! as you chose {input_of_user} and computer chose {real_choice_of_computer}')
    elif a is False:
        print(f'You lost.. as you chose {input_of_user} and computer chose {real_choice_of_computer}')
    print('Well played..')
    a = input('Do you want to play again? (y,n): ')
