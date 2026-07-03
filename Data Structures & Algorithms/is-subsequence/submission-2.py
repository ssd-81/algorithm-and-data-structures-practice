class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
        i, j = 0, 0 # i -> s , j -> t

        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        print(i, j)
        return True if i == len(s) else False 