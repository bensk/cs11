score1 = 0
score2 = 0
tiecount = 0
player_1 = raw_input("Player 1, what's your name?")
player_2 = raw_input("Player 2?")

import random

def shuffled_deck():
    deck = range(2,53)
    random.shuffle(deck)
    return deck

deck = shuffled_deck()

def player_turn(player_name):
    card = deck.pop()
    print player_name + " drew a " + str(card)
    return str(card)




while deck:
    if player_turn(player_1) == player_turn(player_2):
        print "It's a tie!"
        tiecount = tiecount + 1
    elif player_turn(player_1) > player_turn(player_2):
        score1 = score1 + 1
        print "Player 1 Wins"
    elif player_turn(player_1) < player_turn(player_2):
        score2 = score2 + 1
        print "It's a tie!"

print score1
print score2
print tiecount