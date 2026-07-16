class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(arr, arr_set):
            if len(arr) == len(nums):
                res.append(arr[:])
                return 
            
            for i in range(len(nums)):
                if i not in arr_set:
                    arr.append(nums[i])
                    arr_set.add(i)
                    backtrack(arr, arr_set)
                    arr.pop()
                    arr_set.remove(i)
            
        backtrack([], set())
        return res 