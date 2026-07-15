from struct import unpack

import nato
from string import ascii_uppercase, ascii_lowercase

nabc=list(nato.phonetic.values()) #nato values
abc=list(ascii_lowercase) #just abc
# print(nabc)
# print(abc)
# print(dict(nato.phonetic.keys())) #nato keys
# print(list(nato.phonetic.values())[0])

def to_nato(words : str) -> str:
    l = []
    for i in words.lower():
        if i.upper() in dict.keys(nato.phonetic):
            print("key found: ",i,)
            l.append(list(nato.phonetic.values())[abc.index(i)])
            print('added :',(list(nato.phonetic.values())[abc.index(i)]))
        if i in ',.?!' :
            l.append(i)
        else:
            continue
    print(' '.join(l))
    return ' '.join(l)


# from ai

# def to_nato(words):
#     result = []
#     for ch in words:
#         if ch == " ":
#             continue
#         if ch.isalpha():
#             result.append(NATO[ch.upper()])
#         else:
#             result.append(ch)
#     return " ".join(result)

# best


# from preloaded import NATO # NATO['A'] == 'Alfa', etc
# from struct import unpack
# from string import ascii_uppercase, ascii_lowercase
# abc=list(ascii_lowercase) #just abc


# def to_nato(words : str) -> str:
#     l=[]
#     for i in words:
#         l.append(NATO[abc.index(i)])
#         if i in ',.?!':
#             l.append(i)
#         else:
#             continue
#     return l


# from preloaded import NATO
#
# def to_nato(words):
#     result = []
#     for ch in words:
#         if ch == " ":
#             continue
#         if ch.isalpha():
#             result.append(NATO[ch.upper()])
#         else:
#             result.append(ch)
#     return " ".join(result)

# final:
# from preloaded import NATO # NATO['A'] == 'Alfa', etc

# def to_nato(words : str) -> str:
#     l=[]
#     for i in words:
#         if i.isalpha():
#             l.append(NATO[i.upper()])
#         elif i != ' ':
#             l.append(i)
#     return ' '.join(l)

# best

# def to_nato(words):
#     return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')