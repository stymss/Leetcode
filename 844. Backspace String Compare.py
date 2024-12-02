class Solution:
    # TC - O(n+m) 
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss, st = [], []

        # Process characters in s
        for char in s:
            if char != '#':
                ss.append(char)
            else:
                if ss:
                    ss.pop()

        # Process characters in t
        for char in t:
            if char != '#':
                st.append(char)
            else:
                if st:
                    st.pop()

        return True if ''.join(ss) == ''.join(st) else False
       