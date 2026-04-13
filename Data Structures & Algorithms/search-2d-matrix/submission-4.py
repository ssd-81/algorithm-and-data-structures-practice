class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if self.binarySearch(i, target):
                return True
        return False
    

    def binarySearch(self, sub: List[int], val: int)-> bool:
        start = 0
        end = len(sub) - 1
         
        while start <= end:
            mid = start + (end - start)//2
            
            if val == sub[mid]:
                return True
            elif val < sub[mid]:
                end = mid - 1
            else: 
                start = mid + 1
        return False 