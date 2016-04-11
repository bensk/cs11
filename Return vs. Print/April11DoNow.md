# April 11 – <code>return</code> vs. <code>print</code>

## Do Now
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

---

## Reading
<code>print</code> just shows the human user a string representing what is going on inside the computer. The computer cannot make use of that printing. <code>return</code> is how a function gives back a value. This value is often unseen by the human user, but it can be used by the computer in further functions.

On a more expansive note, <code>print</code> will not in any way affect a function. It is simply there for the human user's benefit. It is very useful for understanding how a program works and can be used in debugging to check various values in a program without interrupting the program.

> ## Print is for people. Remember that slogan. Printing has no effect on the ongoing execution of a program. It doesn’t assign a value to a variable. It doesn’t return a value from a function.

---

## Guided Practice
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
return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
```

## Check your understanding
```python
def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print h(2)
```
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
- [ ] d) 25
- [ ] e) Error: y has a value but x is an unbound variable insidethe square function

Answer on [this Google form](https://docs.google.com/a/ms223.org/forms/d/1QsTK_Tlw1hIwoJenxGX5beEThv90lWFecT1_fJm_1s8/viewform#start=embed).
