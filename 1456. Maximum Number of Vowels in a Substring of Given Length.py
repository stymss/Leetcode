class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vowels_count_k_window = 0
        max_vowels_count = 0

        for i in range(k):
            if s[i] in vowels:
                vowels_count_k_window += 1
        max_vowels_count = vowels_count_k_window

        for i in range(k, len(s)):
            # remove the effect of the character leaving the window
            if s[i-k] in vowels:
                vowels_count_k_window -= 1
            
            if s[i] in vowels:
                vowels_count_k_window += 1
            
            max_vowels_count = max(max_vowels_count, vowels_count_k_window)
        return max_vowels_count