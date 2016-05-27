---
layout: "post"
title: "Classes Part II"
date: "2016-05-27 22:13"
---

## Do Now

```python
class Pet(object):
    def __init__(self, name):
        self.name = name

my_pet = Pet("Nymeria")
print my_pet.name
```

**Answer in comments:**

1. What do you think `__init__ ` does?`?
2. What if you wanted to initialize all pet objects with a name and a color?
3. How would you modify the code to create a pet object with a name of "Nymeria" and a color of "brown"?

---

## Classes == Blueprints

Classes are like blueprints. When I call the `Pet` class above:    

```python
my_pet = Pet("Nymeria")
```

Python creates a new **object** that is an **instance** of the `Pet` **class**. Let's take a second to absorb that. I can make many `Pet`s by **instantiating** (creating) more **instances**.

- Classes are like blueprints or definitions for "chunks" of code.
- "Instantiate" just means to create an **object** from the **class**.
- The resulting "chunk" is called an object(`Pet("Nymeria")`) and you then assign it to a variable (`my_pet`) to work with it.

**[Last class](http://bsk.education/CS11/2016/05/24/classes/)** we added attributes **after** the class was instantiated, but `self` allows for us to assign attributes at the beginning. When we build classes, we don't want to randomly add attributes. We want to go in with a **blueprint**.

## Practice Objects

```python
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "These lyrics are copywrighted",
                   "So I'll stop here"])

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",])
# This is your daily reminder that Drake is Canadian

happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()
```

#### Why do I need self when I make `__init__ ` or other functions for classes?

If you don't have `self.lyrics`, then code like `lyrics = "Happy birthday to you"` could mean a variable `cheese` or the attribute of a particular object. With `self.lyrics = "Happy birthday to you"` it's clear you mean the attribute `self.lyrics`.

1. Write some more songs using this and make sure you understand that you're passing a list of strings as the lyrics.
2. Modify the class so that it takes in the title and the artist as well as lyrics of a song (hint: you will need to add more `self._____`).
3. Modify the function `sing_me_a_song` so it prints out something like:

```
Spectacular Failure by Lake Street Dive
I can't excuse your behavior
What a spectacular failure
```

#### <span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub in a file called `SongLyrics.py`
