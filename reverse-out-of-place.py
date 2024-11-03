# reversing an array out of place
# [1,2,3,4,5] ---> [5,4,3,2,1]

import numpy as np
def  rev_out_place(arr):
    arr2 = np.zeros(len(arr),dtype=int)
    i=0
    while (i<=len(arr)-1):
        arr2[i]=arr[len(arr)-1-i]
        i+=1
    return arr2

print(rev_out_place(np.array([1,2,3,4,5])))