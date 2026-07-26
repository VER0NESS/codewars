def divizor(l,d):
    res=[]
    for i in l:
        if i%d==0:
            res.append(i)
    print(res)
divizor([1, 2, 3, 4, 5, 6],2)
# [2, 4, 6
def divisible_by(nums, div):
    return [i for i in nums if i%div==0]
divisible_by([1, 2, 3, 4, 5, 6],2)