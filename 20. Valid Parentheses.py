class Solution:
    def isValid(self, s: str) -> bool:
        # if length of s is not even, it can never be balanced
        if len(s) % 2 != 0:
            return False

        paran_mapper = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                # check if stack has some elements or not
                if not stack:
                    return False
                else:
                    # get the top elements
                    top_element = stack[-1]

                    # check if it balances
                    if paran_mapper[char] == top_element:
                        stack.pop()
                    else:
                        return False
        
        # check if the stack is empty or not
        return len(stack) == 0