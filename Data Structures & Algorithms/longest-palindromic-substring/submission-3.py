class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True 
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
        
        for i in range(2, n):
            l = 0
            r = i
            while r < n:
                if s[l] == s[r] and dp[l+1][r-1]:
                    dp[l][r] = True 
                l += 1
                r += 1
        max_length_palindrome = ""
        for i in range(n):
            for j in range(n):
                if dp[i][j] and j - i + 1 > len(max_length_palindrome):
                    max_length_palindrome = s[i:j+1]
        return max_length_palindrome