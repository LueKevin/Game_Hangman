#  03/14/20
#  Hangman game main module

import random

def hangman():
    wordList = ["Python", "Java", "computer", "hacker", "painter"]
    randomNumber = random.randint(0, 4)
    word = wordList[randomNumber]
    wrongGuesses = 0
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|"]
    remainingLetters = list(word)
    letterBoard = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrongGuesses < len(stages) - 1:
        #Game Logic
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:  
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
        
            
hangman()
