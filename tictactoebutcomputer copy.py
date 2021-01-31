import random

import time

board = ['1','2','3','4','5','6','7','8','9']

count = 0

answer = 'y'

i = 0

def boardPrint(board):
    print ('\n\n', board[:3] , '\n\n', board[3:6],'\n\n', board[6:9])


print('The board is shown below. Spots that are still numbers are available. You are playing X')


turn = 'x'

def endGame(board):
    count = 0
    time.sleep(1)
    boardPrint(board)
    board = ['1','2','3','4','5','6','7','8','9']
    time.sleep(1)
    print('GAME OVER\n')
    if turn == 'x':
        print('i guess computers are not always smarter')
    else:
        print('the computer was not even a smart computer why are you so bad')


    

while answer == 'y':
    time.sleep(1)
    boardPrint(board)
    time.sleep(1)
    print('\n',turn, ', it is your turn.')
    time.sleep(1)
    if turn == 'o':
        a = (random.randint(0,9))
        while board[a-1] != str(a):
            a = (random.randint(0,9))
    else:
        a = int(input("where would you like to move?\n"))
    if board[a-1] == str(a):
        if turn == 'o':
            time.sleep(1)
            print('The computer has chosen spot', a)
        board[a-1] = turn
        count += 1
    else:
        print('That spot is not available.')
        continue
    if count >= 5:
        if board[0] == board[1] and board[1] == board[2]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[3] == board[4] and board[4] == board[5]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[6] == board[7] and board[7] == board[8]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[0] == board[3] and board[3] == board[6]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[1] == board[4] and board[4] == board[7]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ') 
        elif board[2] == board[5] and board[5] == board[8]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[0] == board[4] and board[4] == board[8]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
        elif board[6] == board[4] and board[4] == board[2]:
            endGame(board)
            answer = input('would you like to play again? enter y for yes and n for no: ')
    if count > 9:
        boardPrint(board)
        print('GAME OVER\n it was a tie')
        board = ['1','2','3','4','5','6','7','8','9']
        count = 0
        answer = input('would you like to play again? enter y for yes and n for no: ')

    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    i += 1


