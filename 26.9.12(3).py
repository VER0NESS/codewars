def mirror(data: list) -> list:
    return sorted(data) + [int(i) for i in sorted(data)[-2::-1]]
mirror([3,1,2])
# data[-2::-1]
#      │ │ │
#      │ │ └── step = -1        → go backwards
#      │ └──── stop = None      → go all the way to the beginning
#      └────── start = -2       → begin at second-to-last element