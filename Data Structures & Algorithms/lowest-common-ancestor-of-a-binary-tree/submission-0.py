# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if not root:
            return None

        left_sub = self.lowestCommonAncestor(root.left, p, q)
        right_sub = self.lowestCommonAncestor(root.right, p, q)

        if left_sub and right_sub:
            return root 
        
        return left_sub if left_sub else right_sub 