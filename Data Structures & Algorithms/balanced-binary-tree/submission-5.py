# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left_sub = height(node.left)
            right_sub = height(node.right)
            
            if left_sub == -1 or right_sub == -1:
                return -1
            
            if abs(left_sub - right_sub) > 1:
                return -1
            return 1 + max(left_sub, right_sub)
        return height(root) != -1 

