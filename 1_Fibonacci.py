# PRACTICAL 1: FIBONACCI SERIES

# Aim: Write a non-recursive and recursive program to
# calculate Fibonacci numbers and analyze their time
# and space complexity.


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter number of terms: "))

print("Non-recursive:")
fibonacci(n)

print("\nRecursive:")
for i in range(n):
    print(fib(i), end=" ")




# Non-Recursive: Time – O(n), Space – O(1)
# Recursive: Time – O(2ⁿ), Space – O(n).