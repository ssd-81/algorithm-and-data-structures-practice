class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False 
        
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1
        
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        
        for ch in s_map:
            if t_map[ch] < s_map[ch]:
                return False 
            
        return True 