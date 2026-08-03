from operator import index
from string import ascii_lowercase
def words_to_marks(s):
    total = 0
    for i in s:
        total += ([' '] + list(ascii_lowercase)).index(i)
    return total

words_to_marks('love')       #54
words_to_marks('friendship') #108
    # Easy one

def words_to_marks(s):
  return sum(ord(c)-96 for c in s)

def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s
# ord() is an ordinal value of a symbol
# ascii_lowercase is from 96 to 122, so ord(c) - 96
# quite genious