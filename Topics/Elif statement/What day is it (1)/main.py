# the program considers only a special case
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAY_LENGTH = 1440
reference_time_point = int(630)  # Tuesday, 10:30
offset = int(input()) * 60
resulting_time = reference_time_point + offset
if resulting_time < 0:
    print(weekdays[1])
elif 0 <= resulting_time < DAY_LENGTH:
    print(weekdays[2])
else:
    print(weekdays[3])
