'''
problem statement: user will give range like 20-50 etc. and the program should return all the prime numbers between that'''
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_range(start, end):
    if start > end:
        return []
    if end < 2:
        return []
    if start < 2:
        start = 2

    return [n for n in range(start, end + 1) if is_prime(n)]

start = int(input("Enter start point: "))
end = int(input("Enter end point: "))
print(prime_range(start, end))