class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_array = []
        hashMap = {}
        for i in strs: 
            temp = ''.join(sorted(i))
            if  temp in hashMap:
                hashMap[temp].append(i)
            else:
                hashMap[temp] = [i]
        
        for i in hashMap:
            main_array.append(hashMap[i])

        return main_array
