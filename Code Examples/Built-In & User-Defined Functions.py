"""Built-In & User-Defined Functions"""
# Do Now
import random
random.randint(0, 3)
random.randint(0, 3)
print(random.randint(0, 3))
print(random.randint(0, 3))
print(random.randint(0, 3))
# What does randint do?
# What do the values 0 and 3 do? 
# Try changing those numbers, rerun the program, and write down what changed.
# What is the difference between random.randint(0,3) and print(random.randint(0,3))?

# Write a for loop to print only the odd numbers from this list
list = [3,4,7,13,54,32,653,256,1,41,65,83,92,31]

# Now, iterate and turn your loop into a function called find_odds that takes an input and prints the odd numbers in ANY list.
def find_odds(input):

# To exceed standards, create functions to ADD all of the odd numbers in a list. Then create a function to add all of the even numbers in a list. Test your functions using a randomly generated list of numbers.
def odd_sum(input):
def even_sum(input):

# Test your code
import random
my_randoms = random.sample(range(100), 15)
"""
Checklist
Meeting Standards (3)
for loop prints odd numbers from list
function find_odds takes a list, prints odds.

Exceeding Standards (4)
function odd_sum adds up all odd numbers
function even_sum adds up all even numbers
"""
