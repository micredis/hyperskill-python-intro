# Write your code here
import random

print("H A N G M A N")
words = ["python", "java", "swift", "javascript"]
word = random.choice(words)

user_input = input("Guess the word: > ")
if word == user_input:
    print("You survived!")
else:
    print("You lost!")
