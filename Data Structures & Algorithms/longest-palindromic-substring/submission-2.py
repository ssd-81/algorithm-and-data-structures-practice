class Solution:

    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1
            return s[l+1:r]
        
        max_string = ""
        for i in range(len(s)):
            
            single = expand(i, i)
            double = expand(i, i+1)

            cur = single if len(single) > len(double) else double 
            if len(cur) > len(max_string):
                max_string = cur 
        return max_string 