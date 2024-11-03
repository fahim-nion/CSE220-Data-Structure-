# Reverse in place
#without having a new array
# [1,2,3,4,5] ---> [5,4,3,2,1]

import numpy as np
def  rev_in_place(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    return arr
print(rev_in_place(np.array([1,2,3,4,5])))