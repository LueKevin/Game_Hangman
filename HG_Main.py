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
            
hangman()
