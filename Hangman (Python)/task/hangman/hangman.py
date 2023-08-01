# Write your code here
import random

print("H A N G M A N")
print()
words = ["python", "java", "swift", "javascript"]
secret_word = random.choice(words)
lives = 8


def reveal_character(secret_string, guessed_string, letter):
    new_guessed_string = ''
    for s in range(len(secret_string)):
        if secret_string[s] == letter:
            new_guessed_string += letter
        else:
            new_guessed_string += guessed_string[s]
    return new_guessed_string


guessed_word = '-' * len(secret_word)
while lives > 0:
    print(guessed_word)
    character = input("Input a letter: > ")
    if character not in secret_word:
        print("That letter doesn't appear in the word.")
        lives -= 1
    elif character in guessed_word:
        print("No improvements.")
        lives -= 1
    else:
        guessed_word = reveal_character(secret_word, guessed_word, character)
    print()
    if guessed_word == secret_word:
        print(guessed_word)
        print("You guessed the word!")
        print("You survived!")
        break
else:
    print("You lost!")
