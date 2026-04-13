# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # in place 
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
        
    def quickSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return 
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = pairs[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortHelper(pairs, s, left - 1) # left
        self.quickSortHelper(pairs, left + 1, e) # right