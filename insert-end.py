#insert elem at the ending index
#First, check whether insertion is possible. If not, resize the array. Valid places for inserting are index 0 to size.

import numpy as np

def resize_array(arr,new_size):
    new_arr = np.zeros(new_size,dtype=int)
    for i in range(len(arr)):
        new_arr[i]=arr[i]
    return new_arr


def insert_end(arr,size,elem):
    if len(arr) == size:
        arr = resize_array(arr,size+1)
    arr[size]=elem
    return arr

print(insert_end(np.array([1,2,3,4,5]),5,9))