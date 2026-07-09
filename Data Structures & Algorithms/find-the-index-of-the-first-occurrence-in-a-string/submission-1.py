class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

        for i in range(len(haystack)):
            idx_i = i
            for j in range(len(needle)):
                if idx_i >= len(haystack) or haystack[idx_i] != needle[j]:
                    break
                idx_i += 1
                
                if j == len(needle)-1:
                    return i 
        return -1 