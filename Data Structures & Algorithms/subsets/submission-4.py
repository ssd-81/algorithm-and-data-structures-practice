class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking 
        res = []
        n = len(nums)

        def backtrack(nums_list, idx):
            if idx == n:
                res.append(nums_list[:])
                return 
            
            nums_list.append(nums[idx])
            backtrack(nums_list, idx+1)
            nums_list.pop()
            backtrack(nums_list, idx + 1)
    
        backtrack([], 0)
        return res 
