from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # creating a hash map storing words for constant access
        word_set = set(words)
        res = []
        @lru_cache(None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i] 
                suffix = word[i:]
                
                if prefix in word_set:
                    if suffix in word_set or dfs(suffix):
                        return True 
            return False
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res