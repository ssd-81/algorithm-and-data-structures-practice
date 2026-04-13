class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()
        i = n
        while True:
            curr = self.happyVal(i)
            if curr == 1:
                return True
            if curr in hashSet:
                return False
            hashSet.add(curr)
            i = curr
        


    
    def happyVal(self, n):
        val = 0 
        while n > 0:
            val += (n % 10) **2
            n = n // 10
        return val 
