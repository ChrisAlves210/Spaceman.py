import random

def load_word() -> str:
    '''
    Read the required words file and randomly select a secret word.

    Returns:
        str: The secret word for the Spaceman game.
    '''
    with open('words.txt', 'r') as f:
        content = f.read()
    # Support both space-separated and newline-separated formats
    words_list = content.split()
    secret_word = random.choice(words_list)
    return secret_word

from typing import List

def is_word_guessed(secret_word: str, letters_guessed: List[str]) -> bool:
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # Loop through letters in the secret_word and ensure all are guessed
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word: str, letters_guessed: List[str]) -> str:
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # Build a string with correctly guessed letters and underscores for the rest
    display: List[str] = []
    for ch in secret_word:
        if ch in letters_guessed:
            display.append(ch)
        else:
            display.append('_')
    return ' '.join(display)


def is_guess_in_word(guess: str, secret_word: str) -> bool:
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    # Check if the guessed letter is in the secret word
    return guess in secret_word




def spaceman(secret_word: str) -> None:
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    max_incorrect = 7
    letters_guessed: List[str] = []
    incorrect_guesses = 0

    print("Welcome to Spaceman! Guess the mystery word.")
    print(f"You have {max_incorrect} incorrect guesses allowed.")
    print(get_guessed_word(secret_word, letters_guessed))

    while True:
        # Prompt the player for a single-letter guess
        guess = input("Guess a letter: ").strip().lower()

        # Validate single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please input exactly one alphabetic letter.")
            continue

        # Check repeated guess (stretch)
        if guess in letters_guessed:
            print("You already guessed that letter. Try a new one.")
            continue

        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            # Correct guess feedback
            current = get_guessed_word(secret_word, letters_guessed)
            print(f"Correct! {current}")
        else:
            # Incorrect guess feedback and remaining count
            incorrect_guesses += 1
            remaining = max_incorrect - incorrect_guesses
            print(f"Incorrect. You have {remaining} guesses left.")

        # Show current progress
        print(get_guessed_word(secret_word, letters_guessed))

        # Check win
        if is_word_guessed(secret_word, letters_guessed):
            print("You won! Great job.")
            break

        # Check loss
        if incorrect_guesses >= max_incorrect:
            print("You lost. Better luck next time!")
            print(f"The word was: {secret_word}")
            break






#These function calls that will start the game
def play_game() -> None:
    """Entry point to play one or multiple Spaceman games."""
    while True:
        secret_word = load_word().strip().lower()
        spaceman(secret_word)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    play_game()
