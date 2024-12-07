class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # What if robot has to reach the end of the first row or any cell in this row
        # For this there is only one way - to travel straight

        ans = [[0]*n for _ in range(m)]
        for i in range(1):
            for j in range(n):
                ans[i][j] = 1

        # What if robot has to reach the end of the first col or any cell in this col
        # For this there is only one way - to travel straight

        for i in range(m):
            for j in range(1):
                ans[i][j] = 1

        print("ans - ", ans)

        # Now, number of ways to reach any cell = No of ways to reach top cell + No of ways to reach left cell
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]


        return ans[m-1][n-1]
    