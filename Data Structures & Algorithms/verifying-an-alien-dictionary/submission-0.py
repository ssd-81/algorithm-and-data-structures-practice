class Solution:       

    def dict_order(self, order: str):
        hash_map = {}
        for i in range(len(order)):
            hash_map[order[i]] = i 

        return hash_map 

    def compare(self, hashMap, str1, str2):
        min_ = min(len(str1), len(str2))
        # words=["dag","disk","dog"]
        # order="hlabcdefgijkmnopqrstuvwxyz"
        for i in range(min_):
            if hashMap[str1[i]] != hashMap[str2[i]]:
                if hashMap[str1[i]] > hashMap[str2[i]]:
                    return False 
                return True
        return len(str1) <= len(str2) 

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = self.dict_order(order)

        for i in range(len(words)-1):
            if not self.compare(hashMap, words[i], words[i+1]):
                return False 
        return True 