board = ['1','2','3','4','5','6','7','8','9']

count = 0

a = 1


def boardPrint(board):
    print ('\n\n', board[:3] , '\n\n', board[3:6],'\n\n', board[6:9])

def playAgain(board, count, a):
    board = ['1','2','3','4','5','6','7','8','9']
    count = 0
    a = input('would you like to play again? enter 1 for yes and 0 for no: ')


print('The board is shown below. Spots that are still numbers are available.')

boardPrint(board)


turn = input('\nWhich team will go first, x or o? ')

def endGame():
    boardPrint(board)
    print('GAME OVER\n', turn, 'was just better get freaking rekt')

while a == 1:
    boardPrint(board)
    print('\n',turn, ', it is your turn.')
    a = int(input("where would you like to move?\n"))
    if board[a-1] == str(a):
        board[a-1] = turn
        count += 1
    else:
        print('That spot is not available.')
        continue
    if count >= 5:
        if board[0] == board[1] and board[1] == board[2]:
            endGame()
            playAgain(board, count, a)
        elif board[3] == board[4] and board[4] == board[5]:
            endGame()
            playAgain(board, count, a)
        elif board[6] == board[7] and board[7] == board[8]:
            endGame()
            playAgain(board, count, a)
        elif board[0] == board[3] and board[3] == board[6]:
            endGame()
            playAgain(board, count, a)
        elif board[1] == board[4] and board[4] == board[7]:
            endGame()  
            playAgain(board, count, a) 
        elif board[2] == board[5] and board[5] == board[8]:
            endGame()
            playAgain(board, count, a)
        elif board[0] == board[4] and board[4] == board[8]:
            endGame()
            playAgain(board, count, a)
        elif board[6] == board[4] and board[4] == board[2]:
            endGame()
            playAgain(board, count, a)
    if count == 9:
        boardPrint(board)
        print('GAME OVER\n it was a tie')
        playAgain(board, count, a)
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
   
    

