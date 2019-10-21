

from IPython.display import clear_output

def display_board(board):
    clear_output()  
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
test_board =['  '] * 10
display_board(test_board) 





def player_input(): 
    
    marker = " "
    
    while marker != "X" and marker != "O":
        marker = str(input('Player 1:- Choose "X" or "O" ?')).upper()
        
    Player1 = marker
    Player2 = marker
        
    if Player1 == 'X':
        Player2 = 'O'       
    elif Player1 == 'O':
        Player2 = 'X'
               
    return ('Player1 picks-> '+ Player1, Player2 + ' <- Player2')





def place_marker(board, marker, postion):    
    
    board[postion] = marker




def win_check(board, mark):
    
    if  mark == board[1] and mark == board[2] and mark == board[3]:
        return True
    elif mark == board[1] and mark ==board[5] and mark == board[9]:
        return True
    elif mark == board[1] and mark ==board[4] and mark== board[7]:
        return True
    elif mark == board[2] and mark== board[5] and mark == board[8]:
        return True
    elif mark == board[3]and mark == board[6] and mark == board[9]:
        return True
    elif mark == board[3]and mark == board[5] and mark== board[7]:
        return True
    elif mark == board[4] and mark== board[5] and mark == board[6]:
        return True
    elif mark == board[7]and mark == board[8] and mark == board[9]:
        
        return True
    
    return False




import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    




choose_first()




def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False


# In[9]:


def full_board_check(board):
    
    for i in range (1, 10):
        if space_check(board,i):
            return False
        return True





def player_choice(board):
    x = 0
    while x not in range(1,10):
    
        x = int(input('Choose your next position (1-9) ? '))
        if space_check(board,x):
            return x
        return False 




def replay():
    
    PlayAgain = str(input('Do you want to play again? "(y/n)" ')).lower().startwith('y')
    return PlayAgain == 'y'




print('WELCOME TO A GAME OF TIC TAE TOE')
while True:
    
    mainBoard = [' ']*10
    Player1, Player2 = player_input()
    
    WhoseTurn = choose_first()
    print(WhoseTurn + ' will go first')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if WhoseTurn == 'Player 1':
            
            display_board(mainBoard)
            
            position = player_choice(mainBoard)
            
            place_marker(mainBoard,Player1, position)
            
            if win_check(mainBoard, Player1):
                display_board(mainBoard)
                print('PLAYER 1 WON!!!!')
                game_on = False
            else:
                if full_board_check(mainBoard):
                    display_board(mainBoard)
                    print('TIE GAME!')
                    game_on = False
                else:
                    WhoseTurn = 'Player 2'
           
                    display_board(mainBoard)

                    position = player_choice(mainBoard)


                    place_marker(mainBoard,Player2, position)

                if win_check(mainBoard, Player2):
                    display_board(mainBoard)
                    print('PLAYER 2 WON!!!!')
                    game_on = False
                else:
                    if full_board_check(mainBoard):
                        display_board(mainBoard)
                        print('TIE GAME!')
                        game_on = False
                    else:
                        WhoseTurn = 'Player 1'
                        

    if not replay():
        
        break


# In[ ]:




