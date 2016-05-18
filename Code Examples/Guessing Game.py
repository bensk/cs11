user_name = raw_input("What's your name? \n").capitalize()
print "Hello there " + user_name

upper_bound = int(raw_input("What's the largest number you'd like to choose? \n"))

from random import randint

answer = randint(0, upper_bound)

print "Ok, now choose a number between 1 and " + str(upper_bound)
guess = int(raw_input("What's your guess? \n"))
score = 0
while guess != answer:
    # Got it to give me feedback!
    if guess>answer:
        print "Your guess is too high!"
        score = score + 1
    else:
        print "Your guess is too low!"
        score = score + 1
    guess = int(raw_input("What's your guess? \n"))
score = score+1
print "Great job, " + user_name + ", the number was " + str(answer) + ". It only took you " + str(score) + " tries."
# print randint(0,upper_bound) so, that works

concatenate = 'to join' + 'together'