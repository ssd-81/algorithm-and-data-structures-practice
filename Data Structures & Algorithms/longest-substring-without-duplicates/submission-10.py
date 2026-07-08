class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        chars_set = set()
        for r in range(len(s)):
            chars_set.add(s[r])
            print(chars_set)
            while len(chars_set) != (r-l+1):
                chars_set.remove(s[l])
                l += 1
        
        return r-l+1

