class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    
        hash_words = set(words)

        def dfs(word):


            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if (prefix in hash_words and suffix in hash_words) or (prefix in hash_words and dfs(suffix)):
                    return True 
            return False 
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res 