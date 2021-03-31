"""
The aim of this challange is to indentify if a number is a prime
 
With the help of wikipedia I have discovered the "6k ± 1 optimization" which says that 
every prime greater than 3 is of the form 6k ± 1 where k is any integer greater than 0

Another rule that I found was that instead of looking for divisor from 5 to n/2, it is enough
to look for divisors smaller than sqrt(n) becuse then the numbers start to repeat
"""

def is_prime(input):
    from math import sqrt
    if input <= 3:
        return input > 1
    if input % 2 == 0 or input % 3 == 0:
        return False
    for x in range(5, int(sqrt(input)),6):
        if input % x == 0 or input % (x + 2) == 0:
            return False
    return True

print(is_prime(2147483641234123421543565475843)) # False
print(is_prime(2147483647)) # True