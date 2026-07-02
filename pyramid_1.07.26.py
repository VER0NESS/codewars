# Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem: imagine that you have a pyramid built of numbers, like the ones here:
#
# Here
# comes
# the
# task...
#
# Let
# 's say that the '
# slide
# down
# ' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the largest '
# slide
# downs
# ' are 3 + 7 + 4 + 9 = 23, and 10 + 20 + 10 + 90 = 130.
#
# Your
# task is to
# write
# a
# function
# that
# takes
# a
# pyramid
# representation as an
# argument and returns
# its
# largest
# 'slide down'.For
# example:
#
# With
# the
# input[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]], your
# function
# should
# return 23.
# With
# the
# input[[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]], your
# function
# should
# return 130.
#
# By
# the
# way...
#
# Tests
# include
# some
# extraordinarily
# high
# pyramids
# so as you
# can
# guess, brute - force
# method is a
# bad
# idea
# unless
# you
# have
# a
# few
# centuries
# to
# waste.You
# must
# come
# up
# with something more clever than that.


# a=[1,2,3]
# b=[6,4,5]
# c=a+b
# print(c)
# print(sum(c))
# def pyramid(l):
#     t=0
#     for i in range (len(l)):
#         t+=(max(l[i]))
#     print(t)



#idk
# def longest_slide_down(l):
#     # Start from the second-to-last row and move upwards
#     for row in range(len(l) - 2, -1, -1): #wrom where start,where stop,what step; get reversed pyramid
#         for col in range(len(l[row])):#get index for each num in each line
#             # Add the larger of the two adjacent children to the current position
#             l[row][col] += max(l[row + 1][col], l[row + 1][col + 1])
# #             print(l[row][col])
# longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
# pyramid([[1],[2,3],[1,4,5]])
#!!!!!!!!!!!l[row][col] row chooses the line and col chooses the index(exact number)
# longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
# l=[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# for i in range (len(l)-2, -1, -1):
    # print(max(l[i]))

# l=[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3], [1,1,2,1,1], [1,1,1,1,4,1]]
# l=[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# total = 0
# for i in range(len(l)-2,-1,-1):
#     print(l[i])
# print('_______________________________')
# for i in range(len(l)-1,-1,-1):
#     print(l[i])

#final
# def longest_slide_down(l):
#     for line in range(len(l)-2,-1,-1):
#         for index in range(len(l[line])):
#             l[line][index]+=max(l[line+1][index],l[line+1][index+1])
#             print(l[line][index])
# longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
#for cw
def longest_slide_down(l):
    for line in range(len(l)-2,-1,-1):
        for index in range(len(l[line])):
            l[line][index]+=max(l[line+1][index],l[line+1][index+1])
    return l[0][0]
longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
