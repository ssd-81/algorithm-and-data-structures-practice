class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums => n elements 
        # each element in nums (0, 1, 2) reps a color
        # sort the element in place
        # 0 , 1 , 2 (group in this manner)
        # the core idea is to do it inplace

        # [1, 0 , 1 , 2]
        hashSet = {0: 0 , 1: 0, 2:0}
        for i in nums:
            hashSet[i] += 1

        for i in range(hashSet[0]):
            nums[i] = 0
        for i in range(hashSet[0], hashSet[0] + hashSet[1]):
            nums[i] = 1
        for i in range(hashSet[0] + hashSet[1], hashSet[0] + hashSet[1] + hashSet[2]):
            nums[i] = 2
        
        