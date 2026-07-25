class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
       # k , threshold 
       # size k => average greater than or equal to threshold

        l = 0
        res = 0  

        total = 0 

        for r in range(len(arr)):
            total += arr[r]

            if (r - l + 1 == k):
                if total / k >= threshold:
                    res += 1
                total -= arr[l]
                l += 1
        return res 