# We made the computer play itself!

score2 = 0
score=0
turns = input('best of...?')
moves = ['rock','paper','scissors']
import random

print "Let's play a game of rock paper scissors"

computer_gesture2 = random.choice(moves)
for n in range(1,turns):
    computer_gesture = random.choice(moves)

    if computer_gesture2.lower() == 'rock' and computer_gesture == 'scissors' or computer_gesture2.lower()== 'paper' and computer_gesture == 'rock' or computer_gesture2.lower() == 'scissors' and computer_gesture == 'paper':
        print "Computer 1 plays " + computer_gesture
        print "Computer 2 plays " + computer_gesture2
        print "Computer 2 win!"
        score2 = score2 + 1
        computer_gesture2 = random.choice(moves)
    elif computer_gesture2.lower() == computer_gesture:
        print "Computer 1 plays " + computer_gesture
        print "Computer 2 plays " + computer_gesture2
        print "It's a tie!"

        computer_gesture2 = random.choice(moves)
    else:
        print "Computer 1 plays " + computer_gesture
        print "Computer 2 plays " + computer_gesture2
        print "Computer 1 wins!"
        score=score+1
        computer_gesture2 = random.choice(moves)
print "Computer 1 scores " + str(score) + " out of " + str(turns)
print "Computer 2 scores " + str(score2) + " out of " + str(turns)
print "They tied " + str(turns - score - score2) + " times"
if score>score2:
    print "Computer 1 wins by " + str(score-score2) + "!"
else:
    print "Computer 2 wins by " + str(score2-score) + "!"
# print "Your score is " + str(score2) + " out of " + str(turns)
