class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        votes = defaultdict(list)
        voters = set()
        for i, j in trust:
            votes[j].append(i)
            voters.add(i)

        for candidate in votes:
            if len(votes[candidate]) == (n-1):
                if candidate not in voters:
                    return candidate 
        return -1
        