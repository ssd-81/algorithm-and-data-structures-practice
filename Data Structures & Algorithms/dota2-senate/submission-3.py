class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_queue = [0]*len(senate)
        D_queue = [0]*len(senate)
        r_first, r_last = 0, 0 
        d_first, d_last = 0 , 0 

        for i in range(len(senate)):
            if senate[i] == 'R':
                R_queue[r_last] = i
                r_last += 1
            else:
                D_queue[d_last] = i
                d_last += 1 

        while r_first < r_last and d_first < d_last:
            rad, dire = R_queue[r_first], D_queue[d_first]
            r_first += 1
            d_first += 1

            if rad < dire:
                R_queue[r_last] = (rad + len(senate))
                r_last += 1
            else:
                D_queue[d_last] = (dire + len(senate))
                d_last += 1
        return "Radiant" if r_last > r_first else "Dire" 