class Solution:
    def romanToInt(self, s: str) -> int:
        ri_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # get the value of the last character
        int_rep = ri_map[s[-1]]

        # traverse from the back and make decisions
        for i in range(len(s)-2, -1, -1):
            if ri_map[s[i]] >= ri_map[s[i+1]]:
                # add to the previous result
                int_rep += ri_map[s[i]]
            else:
                # subtract from the previous result
                int_rep -= ri_map[s[i]]

        return int_rep