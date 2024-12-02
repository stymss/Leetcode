from typing import List

class Solution:
    # This can be done usng upper bound concept TC - O(logn)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)-1
        ans = letters[0]
        while low <= high:
            mid = low + (high - low)//2
            if ord(letters[mid]) - ord('a') > ord(target) - ord('a'):
                ans = letters[mid]
                high = mid-1
            else:
                low = mid+1
        return ans