class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_count, small_count = 0, 0

        # Traverse each character of the string
        for char in word:
            if char.isupper():
                cap_count += 1
            else:
                small_count += 1

        if cap_count == len(word) and small_count == 0:
            return True
        elif cap_count == 1 and word[0].isupper():
            return True
        elif cap_count == 0 and small_count == len(word):
            return True

        return False
