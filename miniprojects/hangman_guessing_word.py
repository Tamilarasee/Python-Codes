import random
import string

from hangman_word_list import words


def valid_word(words):
    chosen_word = random.choice(words).upper()
    while '-' in chosen_word or ' ' in chosen_word:
        chosen_word = random.choice(words).upper()
    return chosen_word


def play_hangman(won, lost):
    chosen_word = valid_word(words)
    user_word = []
    lives = 5
    used_letters = set()
    print(f"\nGuess this {len(chosen_word)} letter word")
    while lives:
        user_word = [letter if letter in used_letters else '-' for letter in chosen_word]
        if user_word == list(chosen_word):
            print(f'Yay! You have guessed the word {chosen_word} correctly')
            won += 1
            break
        print(f"\nNo.of Lives: {lives}")
        print("Letters used: ", " ".join(used_letters))
        print("Word to be guessed: ", " ".join(user_word))
        guess = input(f'Guess a letter to fill in the blanks: ').upper()
        if guess not in set(string.ascii_uppercase):
            print("Invalid input")
            continue
        if guess in used_letters:
            print(f'You have already tried the letter {guess}')
            continue
        else:
            used_letters.add(guess)
        if guess not in chosen_word:
            print(f"Sorry, {guess} is not in our word")
            lives += -1


    else:
        print(f'You have lost all lives. The correct word is {chosen_word}')
        lost += 1
    return won, lost


if __name__ == "__main__":
    matches, won, lost = 0, 0, 0
    print("Lets begin the game")
    while True:
        choice = input("\nPlay/Quit - Press P/Q: ").lower()
        if choice == 'p':
            matches += 1
            won, lost = play_hangman(won, lost)
        elif choice == 'q':
            print(f"Number of matches played: {matches} \nNumber of games Won: {won} \nNumber of games lost: {lost}")
            print("Thanks for playing!!!")
            break
        else:
            print("Invalid input")
