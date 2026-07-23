# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def generate_inorder(node):
            if not node:
                return res 
            
            if node.left:
                generate_inorder(node.left)
            res.append(node.val)
            if node.right:
                generate_inorder(node.right)
            return res 
        return generate_inorder(root)