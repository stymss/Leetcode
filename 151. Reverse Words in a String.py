class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.strip().split(' ') if word != '']
        return ' '.join(words[::-1])