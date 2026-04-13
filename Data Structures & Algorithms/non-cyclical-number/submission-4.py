class Solution:
    def isHappy(self, n: int) -> bool:
        checked = []
        # sumOfSquares = 0
        while(True):
            n = self.calcValue(n)
            if n == 1:
                return True
            if n in checked:
                return False 
            
            checked.append(n)


    def calcValue(self, n):
        temp = 0 
        while(n > 0):
            curr = n % 10 
            n = n // 10 
            temp += curr * curr 

        return temp 
            