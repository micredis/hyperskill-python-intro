camel_case = input()
snake_case = ''

if camel_case.islower():
    snake_case = camel_case
else:
    for char in camel_case:
        if char.islower():
            snake_case += char
        else:
            snake_case += '_' + char.lower()
print(snake_case)
