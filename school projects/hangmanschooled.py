
def endGame():
    print('\nYou have correctly guessed the word!')

answer = 'y'

while answer == 'y':
    word = input('Enter your choice of word: ')
    charNum = len(word)
    board = ('_' * charNum)
    yummy = ('_' * (charNum + 1))
    indYummy = -1
    numGuesses = 0
    counter = 0
    print('\n\n\n\n\n\n\n\n\n\n\n')
    print('The word has', charNum, 'letters. You have', charNum + 1, 'guesses.\n')
    while counter < charNum:
        if numGuesses >= charNum + 1:
            print('You have run out of guesses! The word was', word, '.')
            break
        else:
            index = -1
            guess = (input('Enter your guess:\n'))
            if guess == word:
                endGame()
                answer = input('\nWould you like to play again? Enter in y for yes and n for no: ')
            if answer == 'y':
                for letter in word:
                    index += 1
                    if letter == guess:
                        new = board[:index] + guess + board[index + 1:]
                        board = new
                        counter +=1
        if answer == 'y':
            if word.count(guess) > 1:
                print("\nThere are", word.count(guess),' ', guess, "'s in the word.", sep = '')
            if word.count(guess) == 1:
                print('\nThere is 1', guess, 'in the word.')
            else:
                numGuesses += 1
                print('\nThere is no', guess, 'in the word.')
                new = board
                indYummy += 1
                newYummy = yummy[:indYummy] + 'X' + yummy[indYummy + 1:]
                yummy = newYummy
                print('\n', yummy)
                print('You have', 6 - numGuesses, 'guess/es left.')
            print('\n', new)
    if answer == 'y':
        endGame()
        answer = input('\nWould you like to play again? Enter in y for yes and n for no: ')
        