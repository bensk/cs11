import random
# inputs:  x (integer), y (integer)
# outputs: int
# 50% returns sum of x and y, 50% returns product of x and y
def mystery_function(x, y):
    random_number = random.randint(0,2)
    if random_number > 0:
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)