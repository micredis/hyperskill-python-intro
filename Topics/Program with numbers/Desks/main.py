# put your python code here
students_in_group_1 = int(input())
students_in_group_2 = int(input())
students_in_group_3 = int(input())
desks_in_class_1 = int(students_in_group_1 / 2 + students_in_group_1 % 2)
desks_in_class_2 = int(students_in_group_2 / 2 + students_in_group_2 % 2)
desks_in_class_3 = int(students_in_group_3 / 2 + students_in_group_3 % 2)
desks_overall = desks_in_class_1 + desks_in_class_2 + desks_in_class_3
print(desks_overall)