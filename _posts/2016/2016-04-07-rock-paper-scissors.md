---
layout: "post"
title: "Rock || Paper || Scissors"
date: "2016-04-07 14:41"
---

```python
# Play Rock || Paper || Scissors

score = 0
turns = input('best of...?')
moves = ['rock','paper','scissors']
import random

print "Let's play a game of rock paper scissors"

# user_gesture = raw_input("What's your move- rock, paper or scissors?")
for n in range(0,turns):
    user_gesture = raw_input("What's your move- rock, paper or scissors?")
    # moved user_gesture to the top of the four loop
    computer_gesture = random.choice(moves)

    if user_gesture.lower() == 'rock' and computer_gesture == 'scissors' or user_gesture.lower()== 'paper' and computer_gesture == 'rock' or user_gesture.lower() == 'scissors' and computer_gesture == 'paper':
        print "Computer plays " + computer_gesture
        print "You win!"
        score = score + 1
        # user_gesture = raw_input("What's your move- rock, paper or scissors?")
    elif user_gesture.lower() == computer_gesture:
        print "Computer plays " + computer_gesture
        print "It's a tie!"
        # user_gesture = raw_input("What's your move- rock, paper or scissors?")
    else:
        print "Computer plays " + computer_gesture
        print "You loose!"
        # user_gesture = raw_input("What's your move- rock, paper or scissors?")

print "Your score is " + str(score) + " out of " + str(turns)
```
