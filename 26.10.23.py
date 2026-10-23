# def array_plus_array(arr1,arr2):
#     num1=""
#     num2=""
#     for i in arr1:
#         num1=num1+str(i)
#     num1=int(num1)
#     for i in arr2:
#         num2=num2+str(i)
#     num2=int(num2)
#     res=num1+num2
#     return res

def array_plus_array(arr1,arr2):
    res=0
    for i in arr1:
        res+=int(i)
    for i in arr2:
        res+=int(i)
    print(res)
array_plus_array([1,2],[2,2])