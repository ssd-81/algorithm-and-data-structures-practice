class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countSub = set()
        resLen = 0 
        l = r = 0 
        while r < len(s):
            
            while s[r] in countSub:
                  countSub.remove(s[l]) 
                  l += 1
            countSub.add(s[r])
            if r - l + 1 > resLen:
                resLen = r - l + 1
            r += 1        
            
        return resLen

