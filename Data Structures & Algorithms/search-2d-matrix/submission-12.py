class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find the row using binary search operation 
        
        rf, rl = 0, len(matrix) - 1
        valExists = False
        while(rf <= rl):

            if target > matrix[rf][-1]:
                rf += 1
            elif target < matrix[rl][0]:
                rl -= 1
            else:
                valExists = True
                break 

        if valExists:
            l, r = 0, len(matrix[rf])
            while(l <= r):
                mid = (l + r) // 2
                if matrix[rf][mid] == target:
                    return True
                elif matrix[rf][mid] < target:
                    l += 1
                elif matrix[rf][mid] > target:
                    r -= 1
        return False 
