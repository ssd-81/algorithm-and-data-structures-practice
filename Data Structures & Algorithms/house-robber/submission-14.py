class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case 

        hashMap = {}
        def take(houses):
            
            if len(houses) == 0:
                return 0 
            if len(houses) in hashMap:
                return hashMap[len(houses)]
            if len(houses) == 2 or len(houses) == 1:
                val = max(houses)
                hashMap[len(houses)] = val
                return val

            val = max(houses[0] + take(houses[2:]), houses[1] + take(houses[3:]))
            hashMap[len(houses)] = val
            return val
        return take(nums)