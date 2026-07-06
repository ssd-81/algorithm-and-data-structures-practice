class Solution:
    def expand(self,s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:

        longest_str = ""
        len_ls = 0 

        for i in range(len(s)):
            first, second = self.expand(s,i,i), self.expand(s, i, i+1)
            if len(first) > len(second):
                if len_ls < len(first):
                    len_ls = len(first)
                    longest_str = first
            else:
                if len_ls < len(second):
                    len_ls = len(second)
                    longest_str = second
        return longest_str         