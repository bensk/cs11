# is_even

def is_even(x):
    if x %2 ==0:
        return True
    else:
        return False

# is_int
def is_int(x):
    if type(x) == int or abs(x-int(x))==0:
        return True
    else:
        return False

# digit_sum
def digit_sum(n):
	x=0
	n=str(n)
	for number in n:
		x = x + int(number)
	return x

# factorial (lazy)
import math
def factorial(x):
    return math.factorial(x)

# is_prime
"""
Define a function called is_prime that takes a number x as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True.
"""
def is_prime(x):
	prime = 0
	if x >= 2:
		for n in range(2,x):
			if x % n == 0:
				prime = prime + 1
		if prime == 0:
			return True
		else:
		    return False
	else:
		return False

def is_prime(x):
	prime = 0
	if x >= 2:
		for n in range(2,x):
			if x % n == 0:
				prime = prime + 1
		if prime == 0:
			return True
		else:
		    return False
	else:
		return False
