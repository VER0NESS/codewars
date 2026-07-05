def f(l):
    c=[]
    r=[]
    for i in l:
        if i not in c:
            c.append(i)
        else:
            r.append(i)
    print(r)
    return r
f(['abc','abc','ss','ss','go'])