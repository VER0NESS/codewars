from argparse import ArgumentTypeError
from dbm import error





def find_a_b(l, c):
    s = set(l)
    for i in l:
        if i == 0:
            if c == 0 and l.count(0) >= 2:
                return [0, 0]
            else:
                continue
        if ((c // i) in s) and (c % i == 0):
            b = c // i
            temp=l.copy()
            temp.remove(i)
            if b in temp:
                return sorted([i, b])
    return None

#normal versions
def find_a_b(numbers,c):
    for i, a in enumerate(numbers, 1):
        for b in numbers[i:]:
            if a * b == c: return [a, b]

# or
from itertools import combinations
def find_a_b(numbers,c):
    return next(([a,b] for a,b in combinations(numbers,2) if a*b==c),None)
# best
import itertools
def find_a_b(numbers, c):
    return next(([a, b] for a, b in itertools.combinations(numbers, 2) if a * b == c), None)