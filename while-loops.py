# Adapted from http://learnpythonthehardway.org/book/ex33.html
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "The list of numbers is now: ", numbers
    print "At the bottom i is %d" % i


print "The list of numbers is: "

for num in numbers:
    print num

