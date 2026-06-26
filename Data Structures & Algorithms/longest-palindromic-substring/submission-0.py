class Solution:
    def longestPalindrome(self, s: str) -> str:
        def spread(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1 
                j += 1
            return s[i+1:j]

        max_palindromic_string_len = 0
        palindromic_string =0  
        for c in range(len(s)):
            call = spread(c,c)
            if len(call) > max_palindromic_string_len:
                palindromic_string = call 
                max_palindromic_string_len = len(call)
            
            call = spread(c, c+1)
            if len(call) > max_palindromic_string_len:
                palindromic_string = call 
                max_palindromic_string_len = len(call)
        return palindromic_string 


