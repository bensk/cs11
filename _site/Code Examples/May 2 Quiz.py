"""
May 2 Quiz
"""

# Max Value

def max_value(x):
	for i in range(x):
		print i

max_value(42)


# Compare Lists
list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]

def compare_lists(x,y):
	for n in x:
		if n > y[x.index(n)]:
			print n
		else:
			print y[x.index(n)]

compare_lists(list1, list2)

# Swapping Stars
def swapping_stars(x):
	for i in range(x)
* - * - * -
- * - * - *
* - * - * -
- * - * - *
* - * - * -
- * - * - *