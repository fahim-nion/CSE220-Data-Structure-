import numpy as np

arr_2D =np.array([[1,5,5,3,2],
    [4,3,0,8,0],
    [4,7,0,3,4],
    [6,9,4,0,1]])

arr_m = np.array([
    [2,3],
    [4,5],
    [6,7]])

#swappinig elem of Mx2 matrix elem

def swap_two_col(arr):
    r,c = arr.shape
    for i in range(r):
        arr[i][0],arr[i][1] = arr[i][1],arr[i][0]
    return arr
#print(swap_two_col(arr_m))


#swapping MxN matrix

def swap_col(arr):
    row,col = arr.shape
    for i in range(row):
        for j in range(col//2):
            arr[i][j],arr[i][col-1-j] = arr[i][col-1-j],arr[i][j]
    return arr
#print(swap_col(arr_2D))


def row_swap(arr):
    r,c = arr.shape
    for i in range(c):
        for j in range(r//2):
            arr[j][i],arr[r-1-j][i] = arr[r-1-j][i],arr[j][i]
    return arr
#print(row_swap(arr_2D))

#Adding elements of the primary diagonal in a square matrix

prime_arr = np.array([[2,3,9],
                    [4,9,0],
                    [2,9,4]
                    ])
def prime_array_sum(arr):
    sum = 0
    r,c = prime_arr.shape
    if r!=c:
        return "No square matrix"
    else:
        for i in range(r):
            sum += arr[i][i]
        return sum

#print(prime_array_sum(prime_arr))



#Matrix Multiplication 

arr1 = np.array([
    [1,2],
    [3,4]
])

arr2 = np.array([
    [5,6],
    [7,8]
])
def matMultiplication(arr1,arr2):
    row1,col1 = arr1.shape
    row2,col2 = arr2.shape
    new = np.zeros((row1,col2),dtype=int)
    if col1!=row2:
        return "Multiplication Not Possible"
    else:
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    new[i][j]+=arr1[i][k]*arr2[k][j]
    return new


print(matMultiplication(arr1,arr2))