# Write your code here
import random

print("H A N G M A N\n")

words = ["python", "java", "swift", "javascript"]
secret_word = random.choice(words)
lives = 8
guessed_word = '-' * len(secret_word)
guessed_letters = set()


def reveal_character(secret_string, guessed_string, letter):
    """
    This function reveals the guessed character in the secret word.
    """
    new_guessed_string = ''
    for s in range(len(secret_string)):
        if secret_string[s] == letter:
            new_guessed_string += letter
        else:
            new_guessed_string += guessed_string[s]
    return new_guessed_string


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
        print(f"You guessed the word {guessed_word}!")
        print("You survived!")
        break
    print()

if lives == 0:
    print("You lost!")
