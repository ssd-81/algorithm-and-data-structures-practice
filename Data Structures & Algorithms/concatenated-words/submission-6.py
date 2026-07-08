class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # creating a hash map storing words for constant access
        hash_map = Counter(words)
        res = []
        cache = {}
        def dfs(word):
            if word in cache:
                return cache[word] 
            for i in range(0, len(word)):
                first = word[:i] 
                second = word[i:]
                if first in hash_map and second in hash_map:
                    cache[word] = True
                    return cache[word]
                if first in hash_map and dfs(second):
                    cache[word] = True
                    return cache[word]
            cache[word] = False 
            return cache[word]
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res