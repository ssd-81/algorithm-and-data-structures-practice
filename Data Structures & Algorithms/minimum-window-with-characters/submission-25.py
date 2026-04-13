class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        res, resLen = "", float("infinity")
        # shouldn't be initialized like this 
        
        need = defaultdict(int)
        for k in t:
            if need.get(k) != True:
                need[k] = 0 
            need[k] += 1
        matches, req = 0, len(need)
        
        have = {}
        for k in s:
            if have.get(k) != True:
                have[k] = 0
        
        l, r = 0, 0
        while(r < len(s)):
            have[s[r]] += 1

            if have[s[r]] == need[s[r]]:
                matches += 1
            if matches == req:
                if r - l + 1 < resLen:
                    res = s[l:r + 1]
                    resLen = len(res)

                while(matches == req and l < r):
                    have[s[l]] -= 1
                    
                    if have[s[l]] < need[s[l]]:
                        matches -= 1
                    l += 1
                    
                    if matches == req:
                        if r - l + 1 < resLen:
                            res = s[l:r + 1]
                            resLen = len(res)
                    
            r += 1
        return res 


