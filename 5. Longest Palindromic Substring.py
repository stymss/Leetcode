class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps, lps_len = "", 0
        lps_start = 0

        # Go through each char and check the palindrome that can be created using it as the center
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r-l+1
                if cur_len > lps_len:
                    lps_len = cur_len
                    lps_start = l
                l-=1
                r+=1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len = r-l+1
                if cur_len > lps_len:
                    lps_len = cur_len
                    lps_start = l
                l-=1
                r+=1
            
            # get the lps
        lps = s[lps_start: lps_start + lps_len]
        return lps