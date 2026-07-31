def stray(arr):
    for i in arr:
        if arr.count(i)<=1:
            print(i)
    pass
# stray([2,2,4,2,2,2])

def stray(arr):
    return min(arr, key=arr.count)