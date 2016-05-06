# Create a function called "find_evens" that prints only even numbers from a list.
import random
my_randoms = random.sample(range(100), 15) # Create a list of 15 random numbers, to test the function.
print my_randoms

def find_evens(list):
	for x in list:
		if x%2==0:
			print x

test_list = [1,3,5,2,6,8,20,453]

find_evens(my_randoms)
