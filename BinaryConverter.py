# Need to put month and date in as integers. Could add some code to convert, like "July" to 7.
date = raw_input("What's the date?").split("/")
# Reimplemented with lists!
m=int(date[0])
d=int(date[1])
y=int(date[2])

def binDate(m,d,y):
   print(bin(m)[2:] + " / " + bin(d)[2:] + " / " +bin(y)[2:]) # Used string slicing to remove the '0b' from the beginning of the numbers
binDate(m,d,y)
