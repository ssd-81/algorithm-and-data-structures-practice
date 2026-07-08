class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # creating a hash map storing words for constant access
        hash_map = Counter(words)

        res = []
        def dfs(word):
            for i in range(0, len(word)):
                first = word[:i] 
                second = word[i:]
                if first in hash_map and second in hash_map:
                    return True 
                if first in hash_map and dfs(second):
                    return True 
            return False 
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res