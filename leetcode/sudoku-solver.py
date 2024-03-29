class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        chars = "123456789"
        def isvalid(row,col,c):
            for i in range(9):
                if board[row][i]==c:
                    return False
                if board[i][col]==c:
                    return False
                if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)]==c:
                    return False
            return True
        
        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==".":
                        for c in chars:
                            if isvalid(i,j,c):
                                board[i][j]=c
                                if solve():
                                    return True
                                board[i][j]="."
                        return False
            return True
        solve()
            