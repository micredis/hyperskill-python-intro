number_of_halls = abs(int(input()))
capacity = abs(int(input()))
number_of_viewers = abs(int(input()))
can_accommodate_everyone = number_of_halls * capacity >= number_of_viewers
print(can_accommodate_everyone)