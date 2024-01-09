class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = 0
        for i in range(len(matrix)):
            if target in matrix[i]:
                c +=1
        return c>0