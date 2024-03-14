class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lst=[[0]*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lst[j][i]=matrix[i][j]
        return lst