class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def palindrome(x):
            return x == x[::-1]
        
        if palindrome(s):
            return True
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if palindrome(temp):
                return True
        return False 