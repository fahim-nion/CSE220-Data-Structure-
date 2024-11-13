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
print(swap_two_col(arr_m))


#swapping MxN matrix

def swap_col(arr):
    row,col = arr.shape
    for i in range(row):
        for j in range(col//2):
            arr[i][j],arr[i][col-1-j] = arr[i][col-1-j],arr[i][j]
    return arr
print(swap_col(arr_2D))


def row_swap(arr):
    r,c = arr.shape
    for i in range(c):
        for j in range(r//2):
            arr[j][i],arr[row-1-j][i] = arr[row-1-j][i],arr[j][i]
    return arr
print(row_swap(arr_2D))