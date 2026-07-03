class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0 
        start = 0 # start station; initially

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # checking if car can reach the next valid station 
            # if tank capacity is positive, it can reach the next station 
            # else, it won't reach the next station 

            if tank < 0:
                # any station between current start station and current station won't 
                # complete the circuit 
                start, tank = i + 1, 0 
        return start  