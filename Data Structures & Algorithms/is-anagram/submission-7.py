class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hash_s = {}
        hash_t = {}
        for i in s:
            if i in hash_s.keys():
                hash_s[i]+=1;
            else:
                hash_s[i] = 1;
        
        for j in t:
            if j in hash_t.keys():
                hash_t[j]+=1;
            else:
                hash_t[j] = 1;

        if(hash_t==hash_s):
            return True
        else:
            return False
        