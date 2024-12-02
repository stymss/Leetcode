class Solution:
    # TC - O(n)
    def climbStairs(self, n: int) -> int:
        # if we have 1 stair, we can reach in 1 step
        if n == 1:
            return 1

        # if we have 2 stairs, we can reach in 2 stairs
        # 2 => 1step + 1step, directly 2 steps
        if n == 2:
            return 2

        # if n == 3, then we have 3 ways and so on
        dp = [0]*n
        dp[0],dp[1] = 1, 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]