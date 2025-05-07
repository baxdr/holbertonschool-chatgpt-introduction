#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given non-negative integer 'n'.
# The factorial of a number is the product of all positive integers less than or equal to that number.
# The function uses recursion to calculate the factorial.

# Parameters:
# n (int): A non-negative integer for which the factorial is to be calculated.

# Returns:
# int: The factorial of the given integer 'n'. If n is 0, the function returns 1 (since 0! = 1).

def factorial(n):
    if n == 0:
        return 1  # Base case: the factorial of 0 is defined as 1.
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Get the number from the command-line arguments (sys.argv)
f = factorial(int(sys.argv[1]))  # Convert the argument to an integer and compute its factorial

print(f)  # Output the calculated factorial value

