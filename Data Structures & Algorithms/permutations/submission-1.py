class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(arr, arr_set):
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            
            for i in range(len(nums)):
                if nums[i]  not in arr_set:
                    arr.append(nums[i])
                    arr_set.add(nums[i])
                    backtrack(arr, arr_set)
                    arr.pop()
                    arr_set.remove(nums[i])
            
        backtrack([], set())
        return res 