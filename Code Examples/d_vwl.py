def de_vowel(a_string):
	# your code goes here
    strng = []
    vowels = ['a','e','i','o','u']
    for n in a_string:
        # if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u':
        if n not in vowels: # more elegant with a list
            strng.append(n)
    return ''.join(strng)

while user_input !=exit: # while loop test
    user_input = "give me a sentence"
    print de_vowel(user_input)

# examples go here
