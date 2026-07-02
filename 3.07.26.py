import string
def lowercase_count(s):
    total=0
    for i in s:
        if i in string.ascii_lowercase:
           total += 1
    return total
# lowercase_count('NFEINfn')

# best is
def lowercase_count(strng):
    return sum(a.islower() for a in strng)

