"""
Write a function `fruit_pluralizer`. It will take in a list of fruit and return nothing. The function should update the values of the list so that the values are plural. If the fruit name ends in a 'y' remove the 'y' and add 'ies', otherwise add an 's'.

1. Create the function contract for `fruit_pluralizer`.
2. Provide a few examples that confirm `fruit_pluralizer` works as expected:
	* Include examples with 'berry'
	* What if the list is empty?
	* What if the fruit ends in 's'?
"""

def fruit_pluralizer(list_of_fruit):
    newFruits = []
    for fruits in list_of_fruit:
        fruits = fruits[0:len(fruits)-1] + "ies"
        print fruits



fruit_pluralizer(['berry'])