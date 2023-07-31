# Write your code here
import random

print("H A N G M A N")
print()
words = ["python", "java", "swift", "javascript"]
secret_word = random.choice(words)
attempt_times = 8


# def show_3_letters(text):
#     abridged_word = ''
#     for i in range(3):
#         abridged_word += word[i]
#     for i in range(3, len(text)):
#         abridged_word += '-'
#     return abridged_word


def reveal_character(secret_string, guessed_string, letter):
    new_guessed_string = ''
    for s in range(len(secret_string)):
        if secret_string[s] == letter:
            new_guessed_string += letter
        else:
            new_guessed_string += guessed_string[s]
    return new_guessed_string


guessed_word = '-' * len(secret_word)
for i in range(attempt_times):
    print(guessed_word)
    character = input("Input a letter: > ")
    if character not in secret_word:
        print("That letter doesn't appear in the word.")
        print()
    else:
        print()
        guessed_word = reveal_character(secret_word, guessed_word, character)


print("Thanks for playing!")


# user_input = input("Guess the word " + show_3_letters(word) + ": > ")
# if word == user_input:
#     print("You survived!")
# else:
#     print("You lost!")

