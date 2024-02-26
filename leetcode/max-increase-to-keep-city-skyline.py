class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # set up constants 
        rows = len(grid)
        cols = len(grid[0])
        max_each_row = [] 
        max_each_col = []
        max_this_row = 0
        max_this_col = 0 
        total = 0 
        # find max each row 
        for row in grid : 
            max_this_row = max(row)
            max_each_row.append(max_this_row)

        # find max each column
        # zip trick here takes the unpacked version of grid (the rows) and zips them 
        # generating the iterators of the columns. We then select each column in turn.  
        for col in zip(*grid) : 
            max_this_col = max(col)
            max_each_col.append(max_this_col)

        # since we only care about contour and not color 
        # we can do a loop update by looping over the grid 
        # for each cell, our update increment is min of (max each row at row, max each col at col) - current cell 
        # We update by this amount for our total       
        for row in range(rows) : 
            for col in range(cols) : 
                total += min(max_each_row[row], max_each_col[col]) - grid[row][col]
        # return when done 
        return total