from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # What if robot has to reach the end of the first row or any cell in this row
        # For this there is only one way - to travel straight and minimum path sum 
        # is equal to the sum of all cells to that particular cell

        m, n = len(grid),len(grid[0])
        ans = [[0]*n for _ in range(m)]
        ans[0][0] = grid[0][0] # first cell has this as minimum path sum

        for i in range(1):
            for j in range(1, n):
                ans[i][j] = grid[i][j] + ans[i][j-1]

        # What if robot has to reach the end of the first col or any cell in this col
        # For this there is only one way - to travel straight and minimum path sum 
        # is equal to the sum of all cells to that particular cell

        for i in range(1, m):
            for j in range(1):
                ans[i][j] = grid[i][j] + ans[i-1][j]

        print("ans - ", ans)

        # Now, number of ways to reach any cell = 
        # min(path sum to reach top cell + current cell weight, path sum to reach left cell + current cell weight)
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = min(ans[i-1][j] + grid[i][j], ans[i][j-1] + grid[i][j])


        return ans[m-1][n-1]