"""
Variables
1. Ask their name
2. Ask their upper bound
3. Guess!
4. Answer!
"""


name = raw_input("What's your name?")
upper_bound = input("What's the biggest number you want to guess?")
import random
answer = random.randint(0,upper_bound)
guess = input("What's your guess?")
print answer
if guess > answer:
    print "Your guess is too high"
