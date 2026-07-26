class Solution:
    def rob(self, nums: List[int]) -> int:
        choices = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            temp = choices[1]
            choices[1] = max(nums[i] + choices[0], choices[1])
            choices[0] = temp 
        return choices[-1]