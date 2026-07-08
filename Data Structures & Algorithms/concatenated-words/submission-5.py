class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # creating a hash map storing words for constant access
        hash_map = Counter(words)

        res = []
        cache = set()
        def dfs(word):
            if word in cache:
                return True 
            for i in range(0, len(word)):
                first = word[:i] 
                second = word[i:]
                if first in hash_map and second in hash_map:
                    cache.add(word)
                    return True 
                if first in hash_map and dfs(second):
                    cache.add(word)
                    return True 
            return False 
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res