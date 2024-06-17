import sys

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

if len(sys.argv) != 2:
    print("USAGE: python prime_number_sequence.py NUMBER")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print(f"The input number ({sys.argv[1]}) should be an integer")
    sys.exit(1)

if n <= 0:
    print(f"{n} should be a positive integer")
    sys.exit(1)

count = 0
number = 2
while count < n:
    if is_prime(number):
        print(f"{number} ")
        count += 1
    number += 1