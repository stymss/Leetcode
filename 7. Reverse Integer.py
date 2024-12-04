class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31-1
        rev_number = 0

        # get sign
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        # logic
        while x:
            rev_number =  rev_number * 10 + x % 10
            if rev_number < int_min or rev_number > int_max:
                return 0
            x //= 10

        return sign * rev_number
        