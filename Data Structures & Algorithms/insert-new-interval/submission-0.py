class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        ns, ne = newInterval
        ce = 0 
        i = 0 
        for interval in intervals:
            start, end = interval 
            i += 1 
            # we are required to check if the interval lies in the current range 
            if ns >= start and ns <= end:
                new_intervals.append([start, max(end, ne)])
                break
            elif ns > ce:
                new_intervals.append([ns, ne])
                break 
            else:
                new_intervals.append(interval)
                ce = new_intervals[-1][1]
                
        
        while i < len(intervals):
            ns, ne = intervals[i]

            if ns >= new_intervals[-1][0] and ns <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(new_intervals[-1][1], ne)
            else:
                new_intervals.append([ns, ne])
            i += 1 
        return new_intervals 