# April 11 – <code>return</code> vs. <code>print</code>

## 🎯 Do Now
**Open up PyCharm. Paste the following code into the editor:**

```python
import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)
```

**In comments:**

1. What happens when your run this code? How do you know what the result was?
2. Keeping the function the same, rewrite the code to print out the value that the function returns.

#### ⭐️ Upload your code to GitHub in a file called <kbd>April11_DoNow.py</kbd> ⭐️



---

## 📖 Reading
<code>print</code> just shows the human user a string representing what is going on inside the computer. The computer cannot make use of that printing. <code>return</code> is how a function gives back a value. This value is often unseen by the human user, but it can be used by the computer in further functions.

On a more expansive note, <code>print</code> will not in any way affect a function. It is simply there for the human user's benefit. It is very useful for understanding how a program works and can be used in debugging to check various values in a program without interrupting the program.

> ## Print is for people. Remember that slogan. Printing has no effect on the ongoing execution of a program. It doesn’t assign a value to a variable. It doesn’t return a value from a function.

---

## 🐍 Guided Practice
#### ⭐️ Make a new file called <kbd>April11_GuidedPractice.py</kbd> ⭐️
```python
# what does this function return ?
def print_only(x):
   y = x * 2
   print y

# how is this one different ?
def return_only(x):
   y = x * 2
   return y

# let's try to use our 2 functions
print "running print_only ..."
print_only(7)

print "running return_only ..."
return_only(7)

print "printing print_only ..."
print print_only(7)

print "printing return_only ..."
print return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
```

### ✅ Check your understanding

**What will the following code output?**

```python
def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print g(h(2))
```

- [ ] a) 2
- [ ] b) 5
- [ ] c) 7
- [ ] d) 10
- [ ] e) Error: y has a value but x is an unbound variable insidethe square function

Answer on [this Google form](https://docs.google.com/a/ms223.org/forms/d/1QsTK_Tlw1hIwoJenxGX5beEThv90lWFecT1_fJm_1s8/viewform#start=embed).

<!-- ## Independent Work
War!

War (Card Game)

1) Create a program that lets a user play the card game ['War'](http://www.pagat.com/war/war.html).

Your game should:

* Start with a given shuffled deck variable (shuffle function comes from python's random library, more details below)
* Ask for player1 and player2's names.
* Have a function `player_turn`, with the contract shown below:

```python
#player_turn: takes in a player name, player_name, and draws/removes a card from the deck, prints "user drew card x", and returns the value
#input: player_name, string
#output: string
```
* Have a function `compare_scores` that takes in the two strings representing the cards drawn and compares the card values. Make sure to write the contract for `compare_scores`!
* For simplicty Jacks will be represented as 11, Queens will be represented as 12, Kings will be represented as 13, and Aces will be represented as 14
* For simplicty the suit does not matter
* Include a while loop that keeps the game running until there are no cards in the deck.
* Keep track of the score.
* Declare the name of the winner and final score at the end of the game.

### Deck Shuffling

While seemingly simple-- shuffling a deck is a somewhat comoplicatd problem. Luckily, Python's random library has a built in shuffle algorithm. Feel free to read the documentation, but we have provided a simple wrapper function that will return to you a shuffled deck of cards.

```python

import random

# shuffled_deck: will returna shuffled deck to the user
#input:
#output: a list representing a shuffled deck
def shuffled_deck():
	basic_deck = range(2, 15) * 4
	random.shuffle(basic_deck)
	return basic_deck
```

###Bonus!
Instead of closing the program when the deck is empty, create a way for the user to play again. -->
