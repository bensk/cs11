---
layout: "post"
title: "Dictionary Methods"
date: "2016-05-17 18:39"
---

## Do Now

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

The second argument in `.pop(___,___)` is described as the **default value**. This is the value that will be returned if the first argument is **not** in the dictionary.



## Mini-Lesson
> If you're searching for a value in a dictionary and you use a for loop, you're doing it wrong. Stop, go back, and read the previous statement.

```python
dict['key'] = "update or add the value of a key"
dict.clear() # clear values of a dictionary
del dict['Name'] # remove entry with key 'Name'
del dict         # delete entire dictionary
dict.pop(key[, default]) # removes the entry and returns the value


## Check Yourself
- How do we remove an item from a dictionary?
- How do we add items to a dictionary?
- How do we update items in a dictionary?
- Why do we use `None`?
