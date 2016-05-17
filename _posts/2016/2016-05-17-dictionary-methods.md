---
layout: "post"
title: "Dictionary Methods"
date: "2016-05-17 18:39"
---

## <span class="mega-octicon octicon-clock"></span> Do Now (In Google Classroom)

How are dictionaries similar to lists? How are they different?

_When you've finished answering the Do Now, take a look at this code before we start the mini lesson._

<span class="mega-octicon octicon-file-code"></span>
In PyCharm, create a file called `May 17 Do Now_Dictionaries`

Type and run the following code in the interpreter:

```python
my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'delicious'
print my_dictionary
```

What does the second line do?


Type and run the following code in the interpreter:

```python
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print my_dictionary
```

What is the first line?
What does the second line do?

Run the following code:

```python
my_dictionary = {
    'hello': 'hola',
    'goodbye': 'adios'
    }
print my_dictionary.pop('foo', None)
# None
print my_dictionary
# {'goodbye': 2}
```

Then run:

```python
my_dictionary = {
    'hello': 'hola',
    'goodbye': 'adios'
    }
print my_dictionary.pop('foo')
print my_dictionary
```

You get an error, right?

```python
# In comments: What is different between
my_dictionary.pop('foo', None) # and
print my_dictionary.pop('foo')`?
```

## <span class="mega-octicon octicon-mortar-board"></span> Mini-Lesson
> If you're searching for a value in a dictionary and you use a for loop, you're doing it wrong. Stop, go back, and read the previous statement.

The second argument in `.pop(___,___)` is described as the **default value**. This is the value that will be returned if the first argument is **not** in the dictionary.

```python
dict['key'] = "update or add the value of a key"
dict.clear() # clear values of a dictionary
del dict['Name'] # remove entry with key 'Name'
del dict         # delete entire dictionary
dict.pop(key[, default]) # removes the entry and returns the value
```

## <span class="mega-octicon octicon-verified"></span> Check Yourself
- How do we remove an item from a dictionary?
- How do we add items to a dictionary?
- How do we update items in a dictionary?
- Why do we use `None`?

## <span class="mega-octicon octicon-list-ordered"></span> Word Counter App

In this lab we will implement a word frequency algorithm. It will tell you how many of each word you had in an essay.

Make a variable for user input, something like

```python
text_input = raw_input("Paste your text here")
```

In order to turn this text into a list of lower case words we will use the `split("")`, ``replace()``, and `lower()` functions.


For each word in the document, count the number of times it occurs.

Consider the following phrase: 'Cats are cool. Baby cats are called kittens. Cats make great pets.'

The word 'cats' appears 3 times. The word 'are' appears 2 times.
The program will first create a dictionary with the words as keys and the number of times they occur as values.

Then it will prompt the user which word they are curious about. If the word was in the paragraph it will print the number of times it occurred.

#### <span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub in a file called `Word Counter`
