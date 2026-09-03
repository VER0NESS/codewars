def multiples(a: int, b: int, limit: int) -> list[int]:
    res=[]
    for i in range(limit):
        if i==0:
            continue
        if (i%a==0) and (i%b==0):
            res.append(i)
    if limit%a==0 and limit%b==0:
        res.append(limit)
    print(res)
multiples(2,4,40)



#best
def multiples(a: int, b: int, limit: int) -> list[int]:
    return [x for x in range(1, limit + 1) if not x % a and not x % b]






# 1, 5, 15 --> [5, 10, 15]
# 3, 5, 15 --> [15]
# 3, 5, 40 --> [15, 30]
# 2, 4, 40 --> [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]