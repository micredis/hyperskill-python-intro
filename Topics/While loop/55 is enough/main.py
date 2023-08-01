# put your code here
n = int(input())
count = 0
summ = 0
while n != 55:
    count += 1
    summ += n
    n = int(input())
print(count)
print(summ)
print(round(summ / count))  # average
