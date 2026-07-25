class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)

        for word in strs:
            anagramMap["".join(sorted(word))].append(word)
        
        res = []
        for key in anagramMap:
            res.append(anagramMap[key])
        return res 


