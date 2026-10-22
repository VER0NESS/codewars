def check_exam(arr1,arr2):
    res=0
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            res+=4
        elif arr2[i]=="":
            pass
        else:
            res-=1
    print(res)


def check_exam(arr1,arr2):
    return max(0,sum(4 if x==y else(0 if y=="" else -1)for x,y in zip(arr1,arr2)))
# print(check_exam(["a", "a", "c", "b"],["a", "a", "b", "" ]))


# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# # 1. Using zip in a for-loop
# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

# # 2. Converting to a list of tuples
# combined_list = list(zip(names, scores))
# print(combined_list) 
# # Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# # 3. Converting to a dictionary
# score_dict = dict(zip(names, scores))
# print(score_dict) 
# # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
