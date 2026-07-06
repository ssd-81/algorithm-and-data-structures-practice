class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_queue = deque()
        D_queue = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                R_queue.append(i)
            else:
                D_queue.append(i)

        while R_queue and D_queue:
            rad, dire = R_queue.popleft(), D_queue.popleft()

            if rad < dire:
                R_queue.append(rad + len(senate))
            else:
                D_queue.append(dire + len(senate))
        return "Radiant" if R_queue else D_queue 