class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radQueue = deque()
        direQueue = deque()


        for i in range(len(senate)):
            if senate[i] == "R":
                radQueue.append(i)
            else:
                direQueue.append(i)
            
        
        while radQueue and direQueue:
            rCandidate = radQueue.popleft()
            dCandidate = direQueue.popleft()

            if rCandidate < dCandidate:
                radQueue.append(rCandidate + len(senate))
            else:
                direQueue.append(dCandidate + len(senate))
        return "Radiant" if radQueue else "Dire"
            
