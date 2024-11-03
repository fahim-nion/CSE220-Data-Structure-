# Right Shifting
# [1,2,3,4,5] ---> [0,1,2,3,4]

import numpy as np
def  right_shift(arr):
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0] = 0
    return arr

print(right_shift(np.array([1,2,3,4,5])))