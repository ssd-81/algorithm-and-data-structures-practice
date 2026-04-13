class Solution:
    def rob(self, nums: List[int]) -> int:
        # trying to write the solution code from memory 
        # I have not understood the idea yet
        rob1, rob2 = 0, 0 

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 
        