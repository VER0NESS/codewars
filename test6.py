from string import ascii_lowercase

def switcher(arr):
    rabc = [' '] + list(ascii_lowercase[::-1])
    result = []
    for item in arr:
        i = int(item)
        if 0 <= i <= 26:
            result.append(rabc[i])
        elif 27 <= i <= 29:
            result.append("!? "[i - 27])
    return ''.join(result)

# final good
from string import ascii_lowercase
def switcher(arr):
    c = " " + ascii_lowercase[::-1] + "!? "
    return ''.join(c[int(x)] for x in arr)

# best is

chars = "_zyxwvutsrqponmlkjihgfedcba!? "
def switcher(arr):
    return "".join(chars[int(i)] for i in arr if i != "0")

