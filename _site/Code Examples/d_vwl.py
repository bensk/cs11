def de_vowel(a_string):
	# your code goes here
	strng = []
	vowels = ['a','e','i','o','u']
	for n in a_string:
        # if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u':
		if n.lower() not in vowels: # more elegant with a list
			strng.append(n)
	return ''.join(strng)

user_input = raw_input("give me a sentence \n")

while user_input != 'EXIT': # while loop test
	print de_vowel(user_input)
	user_input = raw_input("give me a sentence \n")

# examples go here
# forgot to add .lower(), so it passed all capital vowels