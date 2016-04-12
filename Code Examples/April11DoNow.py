"""
Open up PyCharm. Paste the following code into the editor:
"""

import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)

"""
What happens when your run this code? How do you know what the result was?
Keeping the function the same, rewrite the code to print out the value that the function returns.
"""
