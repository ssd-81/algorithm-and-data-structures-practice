class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            mid = l + (r - l) // 2 

            if self.isValid(piles, h, mid):
                res = mid 
                r = mid - 1
            else:
                l = mid + 1 
        return res 

    
    def isValid(self, p: List[int], h: int, k : int) -> bool:

        totalTime = 0
        for i in p:
            if i % k == 0:
                totalTime += i // k
            else:
                totalTime += i // k + 1
        return True if totalTime <= h else False