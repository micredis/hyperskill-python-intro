import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    n_sqrt = int(math.sqrt(n))
    for i in range(3, n_sqrt + 1, 2):
        if n % i == 0:
            return False
    return True


number = int(input())
if is_prime(number):
    print("This number is prime")
else:
    print("This number is not prime")
