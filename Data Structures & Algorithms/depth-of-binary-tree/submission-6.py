# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using bfs
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0 

        print(q)
        print(len(q))

        while q:
            qLen = len(q)

            for i in range(qLen):
                newNode = q.popleft()
                if newNode:
                    if newNode.left:
                        q.append(newNode.left)
                    if newNode.right:
                        q.append(newNode.right)
            print(q)
            print(len(q))
            depth += 1
        return depth 