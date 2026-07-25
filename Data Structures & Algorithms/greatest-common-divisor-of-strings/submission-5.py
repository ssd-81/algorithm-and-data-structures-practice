class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = str1 if len(str1)>=len(str2) else str2 
        y = str1 if len(str1)<len(str2) else str2

        
        for i in range(len(y), 0, -1):
            if len(x) % len(y[:i]) == 0 and len(y) % len(y[:i]) == 0:
                if y[:i] * (len(y)//len(y[:i])) == y and y[:i] * (len(x)//len(y[:i])) == x:
                    return y[:i]
        
        return ""