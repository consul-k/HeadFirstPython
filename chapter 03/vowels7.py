vowels = {'a', 'e', 'i', 'o', 'u'}
word = set(input("Provide a word to search for vowels: "))

found = vowels.intersection(word)
for vowel in found:
    print(vowel)
