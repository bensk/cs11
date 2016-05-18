text_input = raw_input("Paste your text here \n")
text_input=text_input.lower()
text_input=text_input.split(" ")
key_words = raw_input("What words do you want to search for? \n").split()
my_dictionary={}
"""
Thought I needed this...
for n in key_words:
     my_dictionary[n] = 0
print my_dictionary
print text_input
...I did not
"""
for n in text_input:
    if n in key_words:
        my_dictionary[n]=text_input.count(n)

print "Here's the words you're curious about: \n"
print my_dictionary
