# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        if min_val <= root.val <= max_val:
            return root
        elif root.val < min_val:
            result = self.lowestCommonAncestor(root.right, p, q)
        else:
            result = self.lowestCommonAncestor(root.left, p, q)
        return result
        