from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sn1, sn2 = set(nums1), set(nums2)

        out = []
        for n in sn1:
            if n in sn2:
                out.append(n)
        
        return out