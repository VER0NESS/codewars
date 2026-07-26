def add(lst):
    r = []
    t = 0
    for i in lst:
        t += i
        r.append(t)
    print(r)

def add(l):
    return [sum(l[:i+1]) for i in range(len(l))]

    # 1) sum(l[:i + 1]) slice that sums every value of i to other i already in list
    # 2) for i in range(len(l)) where len(l) produces 0, 1, 2, 3, 4

# slice
# sequence[start:stop:step]

# start: where to begin (inclusive)
# stop: where to end (exclusive)
# # step: how many positions to move each time (default is 1)

# cumulative sum