"""
Dictionaries of List
"""

list_dictionaries = {
 'cat': [1, 3, 4],
 'is': [1, 2, 3, 4]
}
print list_dictionaries
# What type of data is list_dictionaries?
# What type of data are list_dictionaries keys?
# What type of data are list_dictionaries values??
# Update the value of 'is' to [1, 2, 3, 4, 5]
print "*******"
print type(list_dictionaries)
print type('cat')
print type(list_dictionaries['is'])
list_dictionaries['is'].append(5)
print list_dictionaries
