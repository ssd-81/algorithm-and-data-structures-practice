class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in s1:
            s1Count[ord(i) - ord('a')] += 1
        
        for i in range(len(s1)):
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        print(matches)
        
        l = 0 
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            print("l :", l)
            print("r :", r)
            print("s1: ", s1)
            print("s2: ", s2[l:r])
            print(matches) 
            # print(s1Count)
            # print(s2Count)
            
            idx2 = ord(s2[r]) - ord('a')
            s2Count[idx2] += 1
            if s2Count[idx2] == s1Count[idx2]:
                matches += 1
            elif s2Count[idx2] == s1Count[idx2] + 1:
                matches -= 1
            print("matches 1: ", matches)

            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] + 1 == s1Count[idx]:
                matches -= 1
            print("matches 2: ", matches)
            print("------------------------")
            
            l += 1

            
        return matches == 26

