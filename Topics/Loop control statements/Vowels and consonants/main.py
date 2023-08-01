VOWELS = 'a', 'e', 'i', 'o', 'u'
text = input()
for character in text:
    if character in VOWELS and character.isalpha():
        print("vowel")
    elif character.isalpha():
        print("consonant")
    else:
        break
