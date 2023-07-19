#  You can experiment here, it won’t be checked
# Locate a point on the Cartesian coordinate plane:
# which of the four quadrants does a point belong to?
#
# Read two numbers from the input, not necessarily integers,
# the first number will indicate a position on the X-axis,
# the second one — on the Y-axis. Let's keep referring to
# the quadrants by Roman numerals, as shown in the picture.
#
# If the point is the origin (0, 0), print "It's the origin!"
# If a point lies on the axes, with either x = 0 or y = 0,
# print "One of the coordinates is equal to zero!"
#
# Sample Input 1:
# 3.987
# -10
#
# Sample Output 1:
# IV

x = float(input())
y = float(input())
if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
elif x == 0.0 and y == 0.0:
    print("It's the origin!")
else:
    print("One of the coordinates is equal to zero!")  # x == 0 or y == 0