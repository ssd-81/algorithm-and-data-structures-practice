class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first_occurence = self.find_first_occurence(target, nums)
        last_occurence = self.find_last_occurence(target, nums)
        return [first_occurence, last_occurence]
    
    def find_first_occurence(self, target: int, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                r = mid 
        return l if l == r else -1
    
    def find_last_occurence(self, target: int, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2 + 1 # right bias
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid 
        return l if l == r else -1