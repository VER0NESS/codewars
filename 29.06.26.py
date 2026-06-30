# from idlelib.configdialog import is_int


# def outlier(l):
#     for i in l:
#         if ((i%2) == 0) > ((i%2) != 0):
#             print
#         elif ((i%2) == 0) < ((i%2) != 0):
#             None
#
#
# def o(a):
#     evens = [i for i in a if (i%2) == 0]
#     print(evens)
#     odds = [i for i in a if (i%2) != 0]
#     print(odds)
#     if odds > evens :
#         print('odds')
#     if odds < evens :
#         print('evens')
#
# def o(a):
#     if len([i for i in a if (i%2) == 0]) > len([i for i in a if (i%2) != 0]):
#         print([i for i in a if (i%2) != 0])
#     else:
#         print([i for i in a if (i%2) == 0])
# o([1,1,3,3,7,9,2])

#that one works but too heavy for long lists so take this
def o(a):
    odds = [i for i in a if (i%2) != 0] #first i is an integer that will be added to list
    evens = [i for i in a if (i%2) == 0]#try to remember all that bruh
    print((odds[0] if len(odds) < len(evens) else evens[0]))
o([1,1,3,2])

#final result
def find_outlier(a):
    odds = [i for i in a if (i%2) != 0] #first i is an integer that will be added to list
    evens = [i for i in a if (i%2) == 0]#try to remember all that bruh
    return((odds[0] if len(odds) < len(evens) else evens[0]))

#best achievable result that i found
def find_outlier(l):
    p=[n%2 for n in l];return l[p.index(p.count(1)<2)]