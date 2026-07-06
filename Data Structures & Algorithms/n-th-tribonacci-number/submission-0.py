class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]

        if n <= 2:
            return seq[n]
            
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2] + seq[-3])
        
        return seq[-1]