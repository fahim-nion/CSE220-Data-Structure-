#resizing new array

import numpy as np
def resize_array(arr,new_size):
    new_arr = np.zeros(new_size,dtype=int)
    for i in range(len(arr)):
        new_arr[i]=arr[i]
    return new_arr

print(resize_array(np.array([1,2,3,4,5]),10))
