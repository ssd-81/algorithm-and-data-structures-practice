class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking 
        res = []
        n = len(nums)

        def backtrack(nums_list, idx):
            res.append(nums_list[:])
            for i in range(idx, n):
                nums_list.append(nums[i])
                backtrack(nums_list, i + 1)
                nums_list.pop()
    
        backtrack([], 0)
        return res 
