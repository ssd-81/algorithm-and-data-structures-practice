class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        chars_set = set()
        max_len = 0 
        for r in range(len(s)):
            chars_set.add(s[r])
            print(chars_set)
            while len(chars_set) != (r-l+1):
                # chars_set.remove(s[l])
                chars_set.discard(s[l])
                l += 1
            max_len = max(r-l+1, max_len)
        
        return max_len

