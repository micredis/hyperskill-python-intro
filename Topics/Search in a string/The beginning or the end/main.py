text = input()
PATTERN = "old"

pattern_first_occurrence = text.find(PATTERN)
pattern_last_occurrence = text.rfind(PATTERN)

if pattern_first_occurrence > pattern_last_occurrence:
    print(pattern_first_occurrence)
else:
    print(pattern_last_occurrence)
