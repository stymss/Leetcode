class Solution:
    def myAtoi(self, s: str) -> int:
        # remove whitespace chars
        s = s.strip()
        if not s:
            return 0

        # get the sign and remove it for processing
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]

        # check the remaning string
        output = 0
        for char in s:
            if char.isdigit():
                output = output * 10 + int(char)
            else:
                break

        # Apply sign
        output *= sign

        # check output range
        if output < -2**31:
            return -2**31
        elif output > 2**31 - 1:
            return 2**31 - 1

        return output