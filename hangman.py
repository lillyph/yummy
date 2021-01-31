word = input('Enter your choice of word:')
charNum = len(word)
board = ('_' * charNum)
guesses = 0
lol = 0
counter = 0
print('The word has', charNum, 'letters. You have 6 guesses.\n')

def tryHard(board2, counter2, numGuesses2):
    index = -1
    guess = (input('Enter your guess:\n'))
    numGuesses2 += 1
    if guess == word:
        endGame()
    for letter in word:
        index += 1
        if letter == guess:
            new = board2[:index] + guess + board2[index + 1:]
            board2 = new
            counter2 +=1
    print(board2)
    return board2


while counter2 < charNum:
    if numGuesses2 >= 6:
        print('You have run out of guesses! The word was', word, '.')
        break
    else:
        board2 = tryHard(board, counter, guesses)
        board = board2

def endGame():
    print('You have correctly guessed the word!')

    
        






