class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_arr = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            self.prefix_arr[i] = self.prefix_arr[i-1] + nums[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_arr[right+1] - self.prefix_arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)