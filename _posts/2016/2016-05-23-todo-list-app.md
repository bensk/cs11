---
layout: "post"
title: "Todo List App"
date: "2016-05-23 08:21"
---


## <span class="mega-octicon octicon-tasklist"></span> Todo List App

We're going to create to-do list app.

<span class="mega-octicon octicon-file-code"></span>
In PyCharm, create a file called `ToDo`

| Specification  | Points   |
|---|:---:|
|Empty dictionary to store information   |  1 |
|Key for each day of the week   |  1 |
|Each key has a list value that stores items   |  1 |
|User is prompted  |  1 |
|User can type `add` program will ask what day and add it correctly   |  1 |
| User can type `get` and the program will ask for the day and print the values  |  1 |
|**Extensions** | **Points** |
|Use .split() to allow the user to type `get Friday` and see the values|1|
|Use .split() to make `add Friday watch tv and relax` update the list| 1 |
| **Total** | _ / 8 |

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

## Our notes

```python
# some way to add
# some way to read


some_dictionary={
    "monday":[]

    #days of the week
}

def add(action,day):
    # loop this question...
        #append the action to the list value of the day keys
        some_dictionary[day].append(action)
    #until you...
    # I need an option to call choice()

def get(day):
    print some_dictionary[day]
    # I need an option to call choice()

def choice():
    user_choice = raw_input("How can I help you?")
    # if they choose 'add' call add()
    # if they choose 'get' call get()
add("something", "monday")

get("monday")
```

#### <span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub in a file called `ToDo.py`
