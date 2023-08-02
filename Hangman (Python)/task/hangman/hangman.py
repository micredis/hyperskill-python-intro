# Write your code here
import random

WELCOME_PROMPT = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > '
MENU_PROMPTS = ("play", "results", "exit")
MAX_LIVES = 8


def start_menu():
    """
    Start the game menu and handle user choices.
    """
    wins = 0
    loses = 0
    while True:
        option = input(WELCOME_PROMPT)
        if option == MENU_PROMPTS[0]:  # 'play'
            print()
            if start_game():  # if True, i.e. player wins
                wins += 1
            else:  # if player loses
                loses += 1
        elif option == MENU_PROMPTS[1]:  # 'results'
            print(f"You won: {wins} times")
            print(f"You lost: {loses} times")
        elif option == MENU_PROMPTS[2]:  # 'exit'
            break  # End the loop, and thus the function and the game


def reveal_character(secret_string, guessed_string, letter):
    """
    Reveal the guessed character in the secret word.
    """
    new_guessed_string = ''
    for s in range(len(secret_string)):
        if secret_string[s] == letter:
            new_guessed_string += letter
        else:
            new_guessed_string += guessed_string[s]
    return new_guessed_string


def start_game():
    """
    Start a game, return True if player wins, False otherwise.
    """
    words = ["python", "java", "swift", "javascript"]
    secret_word = random.choice(words)
    lives = MAX_LIVES
    guessed_word = '-' * len(secret_word)
    guessed_letters = set()

    while lives > 0:
        print(guessed_word)
        character = input("Input a letter: > ")

        if len(character) != 1:
            print("Please, input a single letter.\n")
            continue

        if not character.isalpha() or not character.islower():
            print("Please, enter a lowercase letter from the English alphabet.\n")
            continue

        if character in guessed_letters:
            print("You've already guessed this letter.")
        elif character not in secret_word:
            print("That letter doesn't appear in the word.")
            lives -= 1
        else:
            guessed_word = reveal_character(secret_word, guessed_word, character)

        guessed_letters.add(character)

        if guessed_word == secret_word:
            print(f"\nYou guessed the word {guessed_word}!")
            print("You survived!")
            return True  # True is for win
        print()

    if lives == 0:
        print("You lost!")
        return False  # False is for loss


print("H A N G M A N")
start_menu()
