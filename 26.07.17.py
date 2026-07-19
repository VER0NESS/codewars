from curses.ascii import isalnum
from importlib.metadata import pass_none
from sqlite3 import sqlite_version
from string import ascii_lowercase
from unittest import skip
from astor.rtrip import convert

def switcher(arr):
        rabc = list(ascii_lowercase[::-1])
        l=[]
        arr=(list(arr.split(',')))
        for i in arr:
                i = int(i)
                print(i,type(i))
                if 0<=i<=26:
                      l.append(rabc[i])
                elif 27<=i<=29:
                        l.append('!? '[i-27])
                else:
                        continue
        print(''.join(l))
# switcher('2,23,5,6,11')   #xcuto
# for i in range(30):
#         switcher(f'{i}')
        #error after 26
# r = ''.join(ascii_lowercase[int(i)] for i in '2,23,5,6,11,'.split(',') if i)
# print(r)

# s = '2,23,5,6,11'
# result = ''.join(ascii_lowercase[int(i)] for i in s.split(',') if i)
# print(result)

# get str of nums return reversed array letters (a=26) + '!? ' = 27 28 29

# for i in reversed(ascii_lowercase):
#         print((i,ascii_lowercase.index(i)))

rabc = [' '] + list(ascii_lowercase[::-1])
print(rabc)

