# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # when iterating the binary tree
        # pass the valid range for the values to the subsequent calls 

        valRange = [float('-inf'), float('inf')]
        def nodeValid(root, ran):
            if not root:
                print("0: that's me")
                return True 
            if root.val <= ran[0] or root.val >= ran[1]:
                print("I was called")
                return False
            
            print("2: we reached here")
            return nodeValid(root.left, [ran[0],root.val]) and nodeValid(root.right, [root.val, ran[1]])
        return nodeValid(root, valRange)