import random


# shuffled_deck: will return a shuffled deck to the user
# input:
# output: a list representing a shuffled deck
def shuffled_deck():
    basic_deck = range(2, 15) * 4
    random.shuffle(basic_deck)
    return basic_deck


# player_turn: takes in a player name, player_name, and draws/removes a card from the deck,
#              prints "user drew card x", and returns the value
# input: player_name, string
# output: string
def player_turn(player_name):
    card = deck.pop()
    print player_name, 'drew card', card
    return str(card)


# p1_card: player 1's card
# p2_card: player 2's card
# Returns the winner's name
# input: p1_card, int
#        p2_card, int
# output: string
def compare_scores(p1_card, p2_card):
    if p1_card > p2_card:
        return player1
    if p2_card > p1_card:
        return player2


# The following are declared in the global scope to allow all functions to reference them
deck = []
player1 = raw_input("What is player 1's name?")
player2 = raw_input("What is player 2's name?")


def play():
    cards = shuffled_deck()
    deck.extend(cards)  # since the deck is empty, we add a new set of shuffled cards each time we play
    p1_score = 0
    p2_score = 0
    while len(deck):
        card1 = player_turn(player1)
        card2 = player_turn(player2)
        winner = compare_scores(card1, card2)
        if winner is player1:
            p1_score += 1
        if winner is player2:
            p2_score += 1

# the deck is now empty again

    print '------'
    print player1, ': score of ', p1_score
    print player2, ': score of ', p2_score

    if p1_score > p2_score:
        print player1 + ' wins!'
    if p2_score > p1_score:
        print player2 + ' wins!'
    if p2_score == p1_score:
        print 'Players tied.'
    print '------'

    redo = raw_input('Type "redo" and hit enter to restart the game, or anything else to quit: ')
    if redo == 'redo':
        play()  # restart the game


play()  # start the game for the first time
