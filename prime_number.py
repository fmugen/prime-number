import sys

if len(sys.argv) != 2 :
    print("USAGE: python prime_number.py NUMBER")
    sys.exit(1)

try: 
    number = int(sys.argv[1])
except ValueError:
    print(f"the input number ({sys.argv[1]}) should be an integer")
    sys.exit(1)

if number < 2:
    print(f"{number} is NOT a prime number")
    sys.exit(1)

prime_number_flag = True

for i in range(2,int(number**0.5) + 1):
    dev = number % i
    if dev == 0:
        print(f"{number} is NOT a prime number. it is devisible by {i}")
        prime_number_flag = False
        break

if prime_number_flag :
    print(f"{number} is a prime number")
