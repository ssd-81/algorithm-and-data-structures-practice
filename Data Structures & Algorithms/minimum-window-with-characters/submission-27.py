class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # shortest_window = ""
        shortest_window = s
        t_map = {}
        for ch in t:
            if ch not in t_map:
                t_map[ch] = 0 
            t_map[ch] += 1
        
        
        matches = 0 
        window_map = defaultdict(int)
        found = False 

        l = 0 
        for r in range(len(s)):
            window_map[s[r]] += 1 

            if s[r] in t_map:
                if window_map[s[r]] == t_map[s[r]]:
                    matches += 1
            
            while matches == len(t_map):
                if not found:
                    found = True 
                if r-l+1 < len(shortest_window):
                    shortest_window = s[l:r+1]
                shortest_window = s[l:r+1]
                window_map[s[l]] -= 1

                if s[l] in t_map and window_map[s[l]] < t_map[s[l]]:
                    matches -= 1 
                l += 1
        return shortest_window if found else ""