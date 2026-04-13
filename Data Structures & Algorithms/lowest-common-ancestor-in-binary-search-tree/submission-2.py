# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the core idea is to find the lowest common descendent
        # of two nodes 
        # both p and q must be descendents of that particular node 
        # a node can be descendent of itself 
        
        # plan of action 
        # iterate through the tree (but how)
        # once a value has been found , don't go further that branch
        # once the other value has been found, return the direct ancestor
        # of the first one 
        
        iter = root
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp 
        while(iter != None):
            if p.val <= iter.val and q.val >= iter.val:
                return iter
            elif p.val < iter.val and q.val < iter.val:
                iter = iter.left 
            else:
                iter = iter.right 








