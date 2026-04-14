class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        max_freq = max_window = 0 

        l = r = 0 

        while r < len(s):
            print(hashMap, "--", s[r])
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1 
            max_freq = max(max_freq, hashMap[s[r]])
            if (r - l + 1) - max_freq > k:
                hashMap[s[l]] -= 1
                l += 1
            max_window = r - l + 1
            r += 1
        return max_window
            
        