#A Game of Rock, Paper, Scissors played against computer
#Author - Babawale Okare
from random import randint

player = input('Select rock, paper or scissors (lowercase) ? ')

print('Player pick->>> ', player, 'vs', end=' ')#end= ' ' function tells the computer to end with a space not a new line

chosen = randint(0, 3)

if chosen == 1:
    computer = 'rock'
elif chosen == 2:
    computer = 'paper'
else:
    computer = 'scissors'

print(computer, '<<<-Computer Pick')

if player == computer:
    print('ITS A DRAW!!!')
elif player == 'rock' and computer == 'scissors':
    print('YOU WIN!!!')
elif player == 'paper' and computer == 'scissors':
    print('COMPUTER WINS!!!')
elif player == 'scissors' and computer == 'rock':
    print('COMPUTER WINS!!!')
elif player == 'scissors' and computer == 'paper':
    print('YOU WIN!!!')
elif player == 'paper' and computer == 'rock':
    print('YOU WIN!!!')
elif player == 'rock' and computer == 'paper':
    print('COMPUTER WINS!!!')







