# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass 

class Solution:
    # TC - O(logn)
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        ans = n+1
        while low <= high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans