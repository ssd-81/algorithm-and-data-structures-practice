class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # storing the characters and their frequency in the current window
        hashMap = {}
        max_freq = window_length = 0 
        left = right = 0 

        while right < len(s):

            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            max_freq = max(max_freq, hashMap[s[right]])

            if (right - left + 1) - max_freq > k:
                hashMap[s[left]] -= 1
                left += 1
            window_length = right - left + 1
            right += 1
        return window_length 
