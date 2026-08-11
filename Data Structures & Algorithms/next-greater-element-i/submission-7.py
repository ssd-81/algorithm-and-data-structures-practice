class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return []
        idx_mapping_2 = {}

        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1][0] < nums2[i]:
                stack.pop()
            
            if stack:
                idx_mapping_2[nums2[i]] = stack[-1][0]
            stack.append((nums2[i], i))

        res = []
        for i in range(len(nums1)):
            if nums1[i] in idx_mapping_2:
                res.append(idx_mapping_2[nums1[i]])
            else:
                res.append(-1)
        return res 