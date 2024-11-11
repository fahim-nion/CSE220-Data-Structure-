import numpy as np

#creating a 2D array

arr = np.zeros((4,5), dtype=int)
print(arr)

'''
 (4,5) here 4 represents row ---> and 5 represents column (down arrow)
'''

#reading elem 
arr[2][3] = 5

print(arr)

#printing row-wise



def print_row(arr):
    row,col = arr_2D.shape
    for i in range(row):
        for j in range(col):
            print(arr_2D[i][j])
        print()
arr_2D =np.array([[1,5,5,3,2],
    [4,3,0,8,0],
    [4,7,0,3,4],
    [6,9,4,0,1]])
# print_row(arr_2D)

#printing column wise

def print_col(arr):
    r,c = arr.shape
    for k in range(c):
        for l in range(r):
            print(arr_2D[l][k])
        print()
#print_col(arr_2D)

#summing all elements----------------------------------------------------

def sum_all(arr):
    sum =0
    row,col = arr.shape
    for i in range(row):
        for j in range(col):
            sum+=arr_2D[i][j]
    return sum
print(sum_all(arr_2D))

#sum every row --------------------------------------------------------

def rowSum(arr):
   # sum = 0
    r,c = arr.shape
    new = np.zeros((r,1),dtype=int)
    for i in range(r):
        for j in range(c):
            new[i][0] +=  arr[i][j]
            # sum+=arr[i][j]
    #     new[i][0] = sum
    #     sum = 0
    return new
print(rowSum(arr_2D))

#sum each column----------------------------------------------------

def sumCol (arr):
   # sum = 0
    r,c = arr.shape
    new = np.zeros((1,c),dtype=int)
    for i in range(c):
        for j in range(r):
            new[0][i] += arr [j][i]
    return new
print(sumCol(arr_2D))
