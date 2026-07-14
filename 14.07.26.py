def expression_matter(a, b, c):
    l=set()
    if all(1 <= i <= 10 for i in (a,b,c)):
        l.add(a+b+c)
        l.add(a+b*c)
        l.add(a*b+c)
        l.add(a*b*c)
        l.add((a+b)*c)
        l.add(a*(b+c))
        print(max(l))
        return max(l)
    else:
        return None

# but best is:
def expression_matter(a, b, c):
    return max(
        a + b + c,
        a + b * c,
        a * b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c)
    )
# or
# expression_matter=lambda a,b,c:max(a+b+c,a+b*c,a*b+c,a*b*c,(a+b)*c,a*(b+c))
# probably should learn lambda