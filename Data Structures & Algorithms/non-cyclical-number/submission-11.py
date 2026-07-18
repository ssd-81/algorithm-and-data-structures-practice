class Solution:
    def isHappy(self, n: int) -> bool:
        leader, trailer = self.sumOfSquares(n), self.sumOfSquares(self.sumOfSquares(n))
        print(leader, trailer)
        while leader != trailer:
            if leader == 1:
                return True
            leader = self.sumOfSquares(self.sumOfSquares(leader))
            trailer = self.sumOfSquares(trailer)
        return leader == 1

    def sumOfSquares(self, n):
        total = 0 

        while n:
            total += (n%10)**2
            n = n // 10 
        return total 