# Write your code here
import random

print("H A N G M A N")
words = ["python", "java", "swift", "javascript"]
word = random.choice(words)


def show_3_letters(text):
    abridged_word = ''
    for i in range(3):
        abridged_word += word[i]
    for i in range(3, len(text)):
        abridged_word += '-'
    return abridged_word


user_input = input("Guess the word " + show_3_letters(word) + ": > ")
if word == user_input:
    print("You survived!")
else:
    print("You lost!")
