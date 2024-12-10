class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = [0]*26

        # If strings are of different sizes, they can never be anagram
        if len(s)!= len(t):
            return False

        # Check for anagram
        for c1, c2 in zip(s, t):
            mapper[ord(c1) - ord('a')] += 1
            mapper[ord(c2) - ord('a')] -= 1

        # For s and t to be anagram, the mapper should have all values as zero
        for num in mapper:
            if num != 0:
                return False

        return True
