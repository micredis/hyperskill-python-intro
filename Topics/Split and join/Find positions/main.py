# put your python code here
numbers = input().split()
x = input()
x_positions = []

counter = 0
for number in numbers:
    if number == x:
        x_positions.append(str(counter))
    counter += 1

if x_positions:    # len(x_positions) != 0
    print(" ".join(x_positions))
else:
    print("not found")
