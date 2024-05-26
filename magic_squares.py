# magic square
from itertools import combinations
import numpy as np

# posibilities = combinations([1,2,3,4,5,6,7,8,9],3)
# count = 0
# for el in posibilities:
#     if el[0] + el[1] + el[2] == 15:
#         print(el)
#         # count += 1
#         # print(count)

# A = [
#         [8,1,6],
#         [3,5,7],
#         [4,9,2]
# ]


# C = np.matmul(A,B)
# print(C)

def rotate_matrix_90(matrix):
    columns = len(matrix)
    rows = len(matrix) - 1
    new_matrix = []

    for i in range(columns):
        new_row = []
        for j in range(rows,-1,-1):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix

def obtain_rotated_matrix(matrix,times):
    array_of_matrix = [matrix]
    for _ in range(times):
        array_of_matrix.append(rotate_matrix_90(array_of_matrix[-1]))
# def reflect_matrix(matrix_for_reflect):
#     qty_of_matrix = len(matrix_for_reflect[0])
#     for matrix in range(qty_of_matrix):
#         array_of_reflected = []
#         for row in matrix:
#             reflected_row = row[::-1]
#         array_of_reflected.append(reflected_row)
#     return array_of_reflected    
        
def reflect_matrix(matrix_for_reflect):
    reflected_row = []
    for row in matrix_for_reflect:
        reflected_row.append(row[::-1])
    return reflected_row

def obtain_reflected_matrix(array_of_matrix):
    reflected_matrix = []
    for matrix in array_of_matrix:
        reflected_matrix.append(reflect_matrix(matrix))
    return reflected_matrix

# Ejemplo de uso
matrix_magic = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2],
]

matrix_given = [
    [4,8,2],
    [4,5,7],
    [6,1,6]
]


rotated = obtain_rotated_matrix(matrix_magic,3)
reflect_rotated = obtain_reflected_matrix(rotated)

allMagicSquares = reflect_rotated + rotated

def distance(matrix_a):
    min_cost = float('inf')
    for matrix in allMagicSquares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(matrix[i][j] - matrix_a[i][j])
        min_cost = min(min_cost,cost)
    return min_cost

a = distance(matrix_given)
print(a)


# for el in allMagicSquares:
#     for row in el:
#         print(row)
#     print("\n")

