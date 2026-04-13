class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointers seem like a good idea
        mergedStr = ""
        endP = min(len(word1), len(word2))
        i = 0 

        while i < endP:
            mergedStr += word1[i] + word2[i]
            i += 1
        if i != len(word2):
            mergedStr += word2[i:]
        if i != len(word1):
            mergedStr += word1[i:]
        return mergedStr 
            