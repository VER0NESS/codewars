def alphabet_war(fight):
    totalr=0
    totall=0
    for i in fight:
        if i in "wpbs":
            totalr+=4 if i=="w" else(3 if i=="p" else(2 if i=="b" else(1 if i=="s" else 0)))
        elif i in "mqdz":
            totall+=4 if i=="m" else(3 if i=="q" else(2 if i=="d" else(1 if i=="z" else 0)))
        print(f"l/r({totall}/{totalr})")
    if totalr>totall:
        print("right wins")
    elif totall>totalr:
        print("right wins")
    else:
        print("equality or error")     
alphabet_war('wwwmmm')