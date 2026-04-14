class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        highest_freq = max_len = 0 
        left = right = 0 

        while right < len(s):

            freqs[s[right]] = freqs.get(s[right], 0) + 1
            highest_freq = max(highest_freq, freqs[s[right]])

            num_chars_to_replace = (right - left + 1) - highest_freq

            if num_chars_to_replace > k:
                freqs[s[left]] -= 1
                left += 1
            max_len = right - left + 1
            right += 1

        return max_len