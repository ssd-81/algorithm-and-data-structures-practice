# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_mapping = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_first, pre_last, in_first, in_last):
            # should this be pre_first >= pre_last
            if pre_first > pre_last:
                return None
            rootVal = preorder[pre_first]
            rootNode = TreeNode(rootVal)

            inorder_idx = inorder_mapping[rootVal]
            left_count = inorder_idx - in_first 

            rootNode.left = build(pre_first + 1, pre_first + left_count, in_first, inorder_idx - 1)
            rootNode.right = build(pre_first + left_count + 1, pre_last, inorder_idx + 1, in_last)

            return rootNode 
        return build(0, len(preorder)-1, 0, len(inorder))



