string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'


def count_occurrences(text, characters):
    characters_tuple = tuple(characters)
    count = 0
    for letter in text:
        if letter in characters_tuple:
            count += 1
    return count


print(count_occurrences(string, vowels))
