def descending_order(num):
    l=[]
    for i in str(num):
        l.append(i)
    l.sort(reverse=True)
    print("".join(l))
descending_order(123)