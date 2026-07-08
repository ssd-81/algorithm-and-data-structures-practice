class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        chars_set = set()
        max_len = 0 
        for r in range(len(s)):
            chars_set.add(s[r])
            while len(chars_set) != (r-l+1):
                if s[l] != s[r]:
                    chars_set.remove(s[l])
                l += 1
            
            max_len = max(max_len, r-l+1)
        return max_len

