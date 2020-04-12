# Hangman Game (Jogo da Forca)
# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Class
class Hangman:
    def __init__(self, word):
        self.word = word
        self.missed_letter = []
        self.guessed_letter = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letter:
            self.guessed_letter.append(letter)
        elif letter not in self.word and letter not in self.missed_letter:
            self.missed_letter.append(letter)
        else:
            return False
        return True

    # Check to end game
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letter) == 6)

    # Check victory
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Hide the word to play the game
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letter:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # User interaction
    def print_game_status(self):
        print(board[len(self.missed_letter)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas:', )
        for letter in self.missed_letter:
            print(letter,)
        print()
        print('Letras corretas:')
        for letter in self.guessed_letter:
            print(letter,)
        print()

def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Principal game execution
def main():
    # Object
    game = Hangman(rand_word())

    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Check the game status
    game.print_game_status()

    if game.hangman_won():
        print('\nParabens, voce venceu!')
    else:
        print('\nGame Over!')
        print('\nA palavra certa era: ' + game.word)

# Program execute
if __name__ == "__main__":
    print(rand_word())
    main()

