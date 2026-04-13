class Solution:
    def trap(self, height: List[int]) -> int:
        
        preMap = [0 for i in range(len(height))]
        postMap = [0 for i in range(len(height))]

        res = 0

        curMax = 0
        for i in range(len(height)):
            preMap[i] = curMax
            curMax = max(curMax, height[i])

        curMax = 0
        for i in range(len(height) - 1, -1, -1):
            postMap[i] = curMax
            curMax = max(curMax, height[i])
        
        print(preMap)
        print(postMap)

        
        for i in range(len(height)):
            curr = min(preMap[i], postMap[i])
            if curr - height[i] > 0:
                res += curr - height[i]
        
        return res 
        
        


        