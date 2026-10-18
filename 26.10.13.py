def solve(s):
    rev = s[::-1]        #reversed s
    res = sum(1 for i in range(len(s)) if rev[i] != s[i])#+to sum if missmatch
    if res == 0:         #if no
        return len(s) % 2 == 1
    return res == 2

solve("abbx")
solve("abba")
solve("abcba")
solve("aa")
solve("ab")

# best is
def solve(s):
    v = sum(s[i] != s[-1-i] for i in range((len(s))//2) )
    return v == 1 or not v and len(s)%2

# print(len("abbx"))                    #=4 

# abbx" ==> true
# // because we can convert 'x' to 'a' and get a palindrome.

# "abba" ==> false
# // because we cannot get a palindrome by changing any character.

# "abcba" ==> true
# // We can change the middle character.

# "aa" ==> false

# "ab" ==> true