class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        result_window = ""
        min_len = float('inf')
        freqMapT = Counter(t)

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j +1]
                tempF = Counter(sub_str)
                
                is_valid = True
                for k, required_count in freqMapT.items():
                    if tempF.get(k, 0) < required_count:
                        is_valid = False
                        break # Not a valid window, move to the next j
                
                if is_valid:
                    current_len = len(sub_str)
                    if current_len < min_len:
                        min_len = current_len
                        result_window = sub_str
        return result_window 
                
                    
                
                


