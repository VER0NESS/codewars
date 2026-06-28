from string import ascii_lowercase
from curses.ascii import isalpha
def is_pangram(st):
    abc = set(ascii_lowercase) #abc of lowercase letters added
    letters = set() #unique collection for letters created
    for i in st.lower():
        if isalpha(i):
            letters.add(i)
    return letters == abc

# from curses.ascii import isalpha
# from string import ascii_lowercase
# def is_pangram(st):
#     abc = set(ascii_lowercase)
#     letters = set()
#     for ch in st.lower():
#         if ch.isalpha():
#             letters.add(ch)
#     return letters == abc

# a = 'FLLMO;MEROMFRE;'   #method test
# for i in a.lower():
#     if isalpha(i):
#         print(i)
