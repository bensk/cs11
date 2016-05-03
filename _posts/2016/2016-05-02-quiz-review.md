---
layout: "post"
title: "<strike>Quiz &</strike> Review"
date: "2016-05-02 16:48"
---

<span class="mega-octicon octicon-file-code"></span>
<kbd>In PyCharm, create a file called <mark>May 2 Quiz</mark></kbd>

1) Write a function, `max_value`, that takes in an integer and prints the numbers from 1 to that number inclusively.

2) Write a function, `compare_lists`, that given two lists of numbers the same length, compares each element of the lists, and print out the higher value at each index.

```python
list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]

compare_lists(list1, list2)
# 4 8 15 16 23 42 should print out
```

3) Write a function, `swapping_stars`, that will print out the following:

```
* - * - * -
- * - * - *
* - * - * -
- * - * - *
* - * - * -
- * - * - *
```

## Extra Credit

Write a function, `find_secret`, that takes in a list of lists and an item. Once it finds the item it will print both indexes of where the item is.

Example:

```python
list_of_lists = [['where', 'is', 'the'],
['very', 'secret', 'word'],
['i', 'can', 'find']
]
secret_item = 'secret'
find_secret(list_of_lists, secret_item) # will print:  1, 1
```

<span class="mega-octicon octicon-mark-github"></span> Upload your code to GitHub! Then return to `d_vwl`.
