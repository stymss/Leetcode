from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            summ = digits[i] + carry
            digits[i] = summ % 10
            carry = summ // 10 if summ > 9 else 0

        if carry:
            digits.insert(0, carry)

        return digits