from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in grouped:
                grouped[sorted_word].append(word)
            else:
                grouped[sorted_word] = [word]
            
        return list(grouped.values())