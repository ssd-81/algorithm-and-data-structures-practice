class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatArr = []
        for i in range(2) :
            for j in nums:
                concatArr.append(j)
        return concatArr