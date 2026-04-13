class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find the row using binary search operation 
        
        rf, rl = 0, len(matrix) - 1
        valExists = False
        while(rf <= rl):
            mid = (rf + rl) // 2
            print("mid: ", mid) 
            if target > matrix[mid][-1]:
                rf += 1
            elif target < matrix[mid][0]:
                rl -= 1
            else:
                print("I have exited")
                valExists = True
                break 

        if valExists:
            l, r = 0, len(matrix[mid]) - 1
            while(l <= r):
                mid2 = l + (r - l) // 2
                print("mid2: ", mid2, "\n", "l:", l, " r:", r)
                if matrix[mid][mid2] == target:
                    return True
                elif matrix[mid][mid2] > target:
                    r = mid2 - 1
                else:
                    l=mid2+1
        return False 
