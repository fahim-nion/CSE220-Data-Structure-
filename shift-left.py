# Left Shifting
# [1,2,3,4,5] ---> [2,3,4,5,0]

import numpy as np
def  left_shift(arr):
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1] = 0
    return arr

print(left_shift(np.array([1,2,3,4,5])))