# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node)->tuple(bool, height):
            if not node:
                return (True, 0)
            
            left_state = check_height(node.left)
            if left_state[0] == False: 
                return (False, -1)  # Propagate the corruption up
                
            right_state = check_height(node.right)
            if right_state[0] == False: 
                return (False, -1)  # Propagate the corruption up
            
            if abs(left_state[1] - right_state[1]) > 1:
                return (False, -1)
            
            return (True, 1 + max(left_state[1], right_state[1]))
        return check_height(root)[0]
            
         

        
