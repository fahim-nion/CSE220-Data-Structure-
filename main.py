import numpy as np
arr = np.array([1,2,3,4,5,6,7],dtype=int)
for i in range( len(arr)):
    if arr[i]%2==0:
        print(arr[i])