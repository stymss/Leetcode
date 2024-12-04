class Solution:
    def isPalindrome(self, x: int) -> bool:
        # initialisations
        rev_num = 0

        # base checks
        # if number is < 0 or ends with 0, it's not a palindrome
        if x < 0 or (x > 9 and x % 10 == 0):
            return False

        # logic
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            x //= 10

        return True if x == rev_num // 10 or x == rev_num else False