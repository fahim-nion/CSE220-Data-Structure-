# Rotate Left
# [1,2,3,4,5] ---> [2,3,4,5,1]

import numpy as np
def  rotate_left(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1] = temp
    return arr

print(rotate_left(np.array([1,2,3,4,5])))