class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        i, j = 0, 0
        def isValid(i, j): # to check co-ordinates
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        while isValid(i, j): # traverse primary diagonal
            ans += mat[i][j]
            mat[i][j] = 0 # replace element with 0 to identify
            i += 1
            j += 1
        
        i, j = len(mat) - 1, 0
        
        while isValid(i, j): # secondary diagonal
            ans += mat[i][j]
            i -= 1
            j += 1

        return ans