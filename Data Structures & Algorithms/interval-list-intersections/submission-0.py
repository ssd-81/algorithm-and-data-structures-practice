class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        common_intervals = []
        while i < len(firstList) and j < len(secondList):
            int1 = firstList[i] 
            int2 = secondList[j]
            print(int1)
            print(int2)
            if int1[0] < int2[0]:
                first, second = int1, int2
            else:
                first, second = int2, int1
            if second[0] <= first[1]:
                common_intervals.append([second[0], min(second[1], first[1])])
            
            if int1[1] < int2[1]:
                i += 1
            else:
                j += 1
        return common_intervals