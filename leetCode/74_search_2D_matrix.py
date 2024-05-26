
# from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         ROWS = len(matrix)
        
#         start, end = 0,ROWS-1
#         while start <= end:
#             row = start + (end-start)//2
#             #greater
#             if target > matrix[row][-1]:
#                 start = row + 1
#             #smaller
#             elif target < matrix[row][0]:
#                 end = row - 1
#             else:
#                 break
#         else:
#             return False
        
#         row_to_search = matrix[row]
#         start,end = 0, len(row_to_search)-1
#         while start <= end:
#             p = start + (end-start)//2
#             if target == row_to_search[p]:
#                 return True
#             elif target > row_to_search[p]:
#                 start = p + 1
#             else:
#                 end = p - 1
#         return False

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 23
# solution1 = Solution()


# print(solution1.searchMatrix(matrix,target))
# # Expected output True



from typing import List

class MatrixSeach:
    @staticmethod
    def search_in_matrix(matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0])
        start,end = 0,ROWS-1
        while start <= end:
            row = (start + end)//2
            # left side
            if target < matrix[row][0]:
                end = row - 1
            elif target > matrix[row][-1]:
                start = row + 1
            else:
                break
        else:
            return False

        row_to_search = matrix[row]
        start, end = 0, COLS-1
        while start <= end:
            mid = (start + end) // 2
            if target == row_to_search[mid]:
                return True
            elif target > row_to_search[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 23

print(MatrixSeach.search_in_matrix(matrix,target))