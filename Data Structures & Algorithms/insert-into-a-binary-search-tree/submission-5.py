# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return TreeNode(val)
        
        iterNode = root

        if iterNode.val > val:
            iterNode.left = self.insertIntoBST(iterNode.left, val)
        elif iterNode.val < val:
            iterNode.right = self.insertIntoBST(iterNode.right, val)
        
        return root 
        