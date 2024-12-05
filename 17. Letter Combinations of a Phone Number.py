from typing import List, Dict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        combs = []
        self.getCombs(digits, letter_map, combs, [], 0)
        return combs
    
    def getCombs(self, digits: str, letter_map: Dict[str, List[str]], combs: List[str], temp: List[str], idx: int):
        # Base Case
        if len(temp) == len(digits):
            combs.append(''.join(temp))
            return

        # logic 
        alphabets = letter_map[digits[idx]]
        for letter in alphabets:
            temp.append(letter)
            self.getCombs(digits, letter_map, combs, temp, idx + 1)
            temp.pop()