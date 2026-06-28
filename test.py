from string import ascii_lowercase
def is_pangram(s):  #s = sentence in brackets
    return all(l in s.lower() for l in ascii_lowercase)
is_pangram("The quick brown fox jumps over the lazy dog")
#import the abc
# #all ===> as I got it, there are two lists:
# a in s.lower(for letters in the sentence)
# and a in the alphabet(ascii_lowercase)
# return checks if all letters from the 1st equal to the 2nd list letters
#so, if they are equal => it's True, and vica versa