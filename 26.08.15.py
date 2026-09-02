def valid_ISBN10(isbn): 
    if (len(isbn)==10)and(isbn.index("X")not in range(0,10)):
        total=0
        for i in range(9):
            total += (1+i)*(int(isbn[i]))
        if total % 11 == 0:
            print('+') 
    if isbn.index("X")==10:
        total+=100
        for i in range(8):
            total += i*(int(isbn[i]))
        if total % 11 == 0:
            print('+')
    else:
        print('-')
valid_ISBN10('123456789X')

#10 digits
#(x*position...)%11=0
#X at the end 

# (x*1+x*2+x*3+x*4+x*5+x*6+x*7+x*8+x*9+x*10)%11=0
# where x = int(isbm[0-9]) if (isbm[0-9])=="X" ===> 10*10

# how to get integers from isbm[] without int()
# for i in range(isbm) 
isbm = "123456789X"

# 1112223339   -->  true
# 111222333    -->  false
# 1112223339X  -->  false
# 1234554321   -->  true
# 1234512345   -->  false
# 048665088X   -->  true
# X123456788   -->  false

# ISBN     : 1 1 1 2 2 2 3 3 3  9
# position : 1 2 3 4 5 6 7 8 9 10

# This is a valid ISBN, because:
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

# print(isbm.index("1"))  value 1 has index 0 
# print(isbm[0])  get 1 on position 0

# final=1*(int(isbm[0]))+1*(int(isbm[1]))+1*(int(isbm[2]))+1*(int(isbm[3]))+1*(int(isbm[4]))+1*(int(isbm[5]))+1*(int(isbm[6]))+1*(int(isbm[7]))+1*(int(isbm[8]))+1*(int(isbm[9]))
# print(final)

def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    if 'X' in isbn:
        if isbn.index('X') != 9:
            return False
    total = 0
    for i in range(10):
        char = isbn[i]
        if char == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += (i + 1) * value
    return total % 11 == 0

def valid_ISBN10(isbn):
    # Check format
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    # Check modulo
    return sum(i*(10 if x=='X' else int(x)) for i,x in enumerate(isbn, 1)) % 11 == 0

# i had a long gap btw but im back