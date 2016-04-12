score = 0
name = raw_input("what's your name?").capitalize()
print "Hey %s! Lets play rock, paper, scissors!" % (name)
rounds = input("How many times would you like to play? Best 2 out of 3? Best 3 out of 5?")
if rounds % 2 == 0:
    print "That wont work! Choose an odd number!"
    rounds = input("How many times would you like to play?")
user_answer = raw_input("Rock, paper or scissors?").lower()
import random
computer_move = ["rock", "paper", "scissors"]
computer = (random.choice(computer_move))
i = 1
while i < rounds:
    if user_answer == "rock" and computer == "paper" or user_answer == "paper" and computer == "scissors" or user_answer == "scissors" and computer == "rock":
        print "Computer drew " + computer
        print "You've lost!"
        user_answer = raw_input("Rock, paper or scissors?").lower()
    elif user_answer == computer:
        print "its a draw!"
        user_answer = raw_input("Rock, paper or scissors?").lower()
    else:
        print "Computer drew " + computer
        print "You've won!"
        score = score + 1
        user_answer = raw_input("Rock, paper or scissors?").lower()

    i = i + 1

print "You won " + str(score) + " out of " + str(rounds) + " times!"
