# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidNode(self, node, left, right):
        if not node:
            return True 
        if left >= node.val or node.val >= right:
            return False 
        
        left_node = self.isValidNode(node.left, left, node.val)
        right_node = self.isValidNode(node.right, node.val, right)
        return left_node and right_node

            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = float('-inf'), float('inf')

        return self.isValidNode(root, left, right)