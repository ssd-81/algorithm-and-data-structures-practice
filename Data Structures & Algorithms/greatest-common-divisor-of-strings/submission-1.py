class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        limitor = str1 if len(str1) < len(str2) else str2
        strentor = str1 if len(str1) > len(str2) else str2
        def valid_divisor(string1, string2):
            
            l = 0 
            for r in range(len(string1)-1, -1, -1):
                if string1[l:r+1] * (len(string2)//(r+1-l)) == string2:
                    return string1[l:r+1]
            return ""
        
        return valid_divisor(limitor, strentor)


