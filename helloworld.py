board = ['1','2','3','4','5','6','7','8','9']

count = 0

i = 0

def boardPrint(board):
    print ('\n\n', board[:3] , '\n\n', board[3:6],'\n\n', board[6:9])

print('The board is shown below. Spots that are still numbers are available.')

boardPrint(board)

turn = input('\nWhich team will go first, x or o? ')

for i in range(69):
    boardPrint(board)
    print(turn, ', it is your turn.')
    a = int(input("where would you like to move?\n"))
    if board[a-1] == str(a):
        board[a-1] = turn
        count += 1
    else:
        print('That spot is not available.')
    if count >= 5:
        if board[0] == board[1] and board[1] == board[2]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[3] == board[4] and board[4] == board[5]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[6] == board[7] and board[7] == board[8]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[0] == board[3] and board[3] == board[6]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[1] == board[4] and board[4] == board[7]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[2] == board[5] and board[5] == board[8]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[0] == board[4] and board[4] == board[8]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
        elif board[6] == board[4] and board[4] == board[2]:
            boardPrint(board)
            print('GAME OVER\n', turn, 'was just better get freaking rekt')
            break
    if count == 9:
        boardPrint(board)
        print('GAME OVER\n it was a tie')
        break
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
    i += 1
    

