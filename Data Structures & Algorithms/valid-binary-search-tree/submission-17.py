# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = -float('inf')
        r = float('inf')

        def inRange(node, l, r):
            # print(l, node.val, r)
            if not node:
                return True 
            if node.val <= l or node.val >= r:
                return False 
            
            return inRange(node.left,l, node.val ) and inRange(node.right,node.val, r)
        return inRange(root, l, r)