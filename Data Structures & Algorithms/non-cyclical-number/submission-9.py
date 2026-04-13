class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.get_square_sum(n)
        fast = self.get_square_sum(self.get_square_sum(n))
        print(slow, fast)
        while slow != fast:
            if fast == 1:
                return True
            slow = self.get_square_sum(slow)
            fast = self.get_square_sum(self.get_square_sum(fast))
            print(slow, fast)
            
        return False if fast != 1 else True
    
    def get_square_sum(self, n):
        val = 0
        while n > 0:
            val += (n % 10)**2
            n = n // 10
        return val