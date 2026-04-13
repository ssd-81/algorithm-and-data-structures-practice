# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []        
        q = deque()
        q.append(root)

        while q:
            level = []
            qLen = len(q)

            for r in range(qLen):

                cur = q.popleft()
                if cur:
                    level.append(cur)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level)
        return len(res) 

