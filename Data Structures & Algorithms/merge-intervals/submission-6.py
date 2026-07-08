class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting intervals based on the first position and then second position 
        intervals.sort(key = lambda k: (k[0], k[1]))

        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]

            if start <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals