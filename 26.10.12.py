def open_or_senior(data):
    res=[]
    for i in data:
        if int(i[0])>=55 and int(i[1])>7  :
            res.append("Senior")
        else:
            res.append("Open")
    return res

# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# best is
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]