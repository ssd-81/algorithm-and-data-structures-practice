class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        
        lst = []
        for i in s:
            lst.append(i)
        for j in t:
            if(j not in lst):
                return False
            else:
                lst.remove(j)
        
        return True
        