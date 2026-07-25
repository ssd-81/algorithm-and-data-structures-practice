class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            freq = [0] * 26 

            for c in word:
                freq[ord(c) - ord('a')] += 1
            freq = tuple(freq) 
            if freq not in anagramMap:
                anagramMap[freq] = []
            anagramMap[freq].append(word)
        return list(anagramMap.values())