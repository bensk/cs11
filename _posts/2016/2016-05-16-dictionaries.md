---
layout: "post"
title: "Dictionaries"
date: "2016-05-16 22:05"
---

## Do Now

<span class="mega-octicon octicon-file-code"></span>
In PyCharm, create a file called `May 16 Do Now_Dictionaries`

Type and run the following code:

```python
my_dictionary = {
'cat': 'a domestic feline',
'dog': 'a domestic canine',
'chair': 'furniture piece for sitting',
'car': 'automobile'
}
print my_dictionary
print my_dictionary['dog']
print my_dictionary.get('dog')
print 'cat' in my_dictionary
print 'monkey' in my_dictionary
```
1. What prints?    
2. What type[^1] is my_dictionary?
3. Add a line of code that will print the definition of `chair`, then run the code again.
4. What happens if you use my_dictionary['kittens']? What do you think that error means?

[^1]: Hint: try `print type(my_dictionary)`

---

## ✍ `Dictionary = { }` ← note curly brackets

Like a list, but has a key instead of an index.
Dictionaries pair the key with a value.

```python
password = {'SK':12345}
```

The key & value can be any string or number.

Dictionaries look like:

```python
passwords = {'SK': 12345, 'Lentino': 67890, 'Perez': 54321}
print passwords['SK']
```

Dictionaries are great for things like **address books** (pairing a name with a phone number), **login pages** (pairing an e-mail address with a username), etc.

## Dictionary Lab
<span class="mega-octicon octicon-file-code"></span>
In PyCharm, create a file called `Dictionary_Lab`

Create a social network profile for yourself using a dictionary. I've suggested some keys, but you should feel free to add your own.

```python
user_profile = {
	# name
	# school
	# birthday
	# email
	# username(s)
	# where are you from?
	# number of siblings
	# skills
	# about you
	# favorite quote
	# favorite movie
	# favorite musician
	# favorite TV show
	# favorite book
}
```

Make sure you can `print` and `return` the correct values for the corresponding key. 

#### <span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub in a file called <kbd>Dictionaries</kbd>
