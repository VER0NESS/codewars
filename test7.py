from string import digits, ascii_lowercase, ascii_uppercase

print(digits)
print(ascii_lowercase)
a=input()
if a.isascii():
    print('+')
else:
    print('-')
