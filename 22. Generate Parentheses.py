from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        parans = []
        self.genParans(n, 0, 0, "", parans)
        return parans
    
    def genParans(self, n, oc, cc, temp, parans):
        # Base Case
        if len(temp) == 2*n:
            parans.append(temp[:])
            return 
        
        # if open count < n, keep appending '('
        if oc < n:
            self.genParans(n, oc+1, cc, temp + '(', parans)

        # keep appending ')' till it's count is less than open count
        if cc < oc:
            self.genParans(n, oc, cc+1, temp + ')', parans)
        