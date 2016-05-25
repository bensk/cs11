---
layout: "post"
title: "Dictionaries of Lists"
date: "2016-05-20 16:38"
---

## <span class="mega-octicon octicon-clock"></span> Do Now (answer in Google Classroom)

<!-- ```python
list_dictionaries = {
 'i': [1, 3, 4],
 'am': [1, 2, 3, 4]
}
print list_dictionaries
# What type of data is list_dictionaries?
# What type of data are list_dictionaries keys?
# What type of data are list_dictionaries values??
# Update the value of 'am' to [1, 2, 3, 4, 5]
``` -->

WITHOUT using PyCharm, predict what is printed by the code below:

```python
this_is_a_dictionary = {"cat":12, "dog":6, "elephant":23}
print this_is_a_dictionary["dog"]
```

---

## <span class="mega-octicon octicon-mortar-board"></span> Mini-Lesson

Last time, we saw that dictionaries can pair keys of any data type with values of any data type. We paired strings with strings last time, but now we're going to pair strings with lists.

Let's review how we **add** values to a dictionary.

```python
list_dictionaries = {
 'i': [1, 3, 4],
 'am': [1, 2, 3, 4]
}

list_dictionaries['groot'] = [1,2,3,4,5]
# update the key 'groot' with a list value
```

What if I know what to add the string `"6"` to the key `"groot"`? How do we add things to a list? `.append()`!

```python
list_dictionaries['groot'].append("six")
```


---

## <span class="mega-octicon octicon-tasklist"></span> Todo List App

We're going to create to-do list app.

<span class="mega-octicon octicon-file-code"></span>
In PyCharm, create a file called `ToDo`

| Specification                                                                 |   Points   |
|:------------------------------------------------------------------------------|:----------:|
| Empty dictionary to store information                                         |     1      |
| Key for each day of the week                                                  |     1      |
| Each key has a list value that stores items                                   |     1      |
| User is prompted                                                              |     1      |
| User can type `add` program will ask what day and add it correctly            |     1      |
| User can type `get` and the program will ask for the day and print the values |     1      |
| **Extensions**                                                                | **Points** |
| Use .split() to allow the user to type `get Friday` and see the values        |     1      |
| Use .split() to make `add Friday watch tv and relax` update the list          |     1      |
| **Total**                                                                     |   _ / 8    |

Example Output

```
What would you like to do?
add
What day?
Friday
What would you like to add to Friday's to-do list?
practice clarinet
What would you like to do?
get
What day?
Friday
You have to practice clarinet.
What would you like to do?
```

#### <span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub in a file called `ToDo.py`
