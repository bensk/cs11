def de_vowel(a_string):
	# your code goes here
    strng = []
    vowels = ['a','e','i','o','u']
    for n in a_string:

        if n != 'a' and n != 'e' and n != 'i' and n != 'o' and n != 'u':
            strng.append(n)
    return ''.join(strng)
print de_vowel(raw_input("Give me a sentence"))

# examples go here

