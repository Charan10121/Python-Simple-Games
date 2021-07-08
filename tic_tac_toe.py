board = [' ']*10
board[0]='x'

def win_check(board,mark):
    if  ((board[1]==board[2]==board[3]==mark!=' ') or (board[5]==board[4]==board[6]==mark!=' ')  or(board[7]==board[8]==board[9]==mark!=' ')  or(board[7]==board[4]==board[1]==mark!=' ')  or(board[2]==board[8]==board[5]==mark!=' ')  or(board[3]==board[9]==board[6]==mark!=' ')  or(board[1]==board[5]==board[9]==mark!=' ')  or(board[7]==board[5]==board[3]==mark!=' ')):
        return True
    return False

def space_full(board,i):
    if board[i]==' ':
        return False
    return True

def board_full(board):
    for i in range(1,10):
        if not space_full(board,i):
            return False
    return True

def place_marker(board,position,mark):
    board[position]=mark

def position_choice(board,mark):
    position=0
    while(position not in [1,2,3,4,5,6,7,8,9] or  ( space_full(board,position)) ):
        position=int(input('Enter a position(1-9): '))
    return position

import random

def who_starts():
    start = random.randint(0,1)
    if start==0:
        return 'Player 1 starts'
    if start==1:
        return 'Player 2 starts'

def display_first_board(board):
    
    print('\n'*100)
    print('(7)'+'|'+'(8)'+'|'+'(9)')   #concatenation takes place
    print('--'+'--'+'--'+'--'+'--'+'--')
    print('(4)'+'|'+'(5)'+'|'+'(6)')
    print('--'+'--'+'--'+'--'+'--'+'--')
    print('(1)'+'|'+'(2)'+'|'+'(3)')

def display_board(board):
    
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])   #concatenation takes place
    print('--'+'--'+'--')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('--'+'--'+'--')
    print(board[1]+'|'+board[2]+'|'+board[3])
    

player1=' '
player2=' '

while(player1!='X' and player1!='O' ):
    player1=(input("Player 1 will be X or O? ")).upper()

if (player1=='X'):
    player2='O'
else:
    player2='X'

starter = who_starts()
print(starter)

check = 0
while True:
    if starter=='Player 1 starts':
        if check==1:
            display_board(board)
        else:
            display_first_board(board)
            check=1
        print("\nPlayer 1's turn")
        position = position_choice(board,player1)
        place_marker(board,position,player1)
        starter='Player 2 starts'

    elif starter=='Player 2 starts':
        if check==1:
            display_board(board)
        else:
            display_first_board(board)
            check=1
        print("\nPlayer 2's turn")
        position= position_choice(board,player2)
        place_marker(board,position,player2)
        starter='Player 1 starts'

    if ( (win_check(board,player1)) or (win_check(board,player2)) or  (board_full(board)) ):
        break


if win_check(board,player1):
    display_board(board)
    print('\nPlayer 1 has won')

elif win_check(board,player2):
    display_board(board)
    print('\nPlayer 2 has won')

elif board_full(board):
    display_board(board)
    print('\nIt is a tie')