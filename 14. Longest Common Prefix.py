from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp, lcp_found = "", False

        # sort the strings based on the length
        sorted_strs = sorted(strs, key = len)

        # get the shortest string
        # lcp can be equal to the length of the shortest string
        shortest_string = sorted_strs[0]

        for i in range(len(shortest_string)):
            alphabet = shortest_string[i]

            # check if this character is in remaining words
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] != alphabet:
                    return lcp 
            
            # if the character matches, add it to the lcp
            lcp += alphabet
        
        return lcp 
