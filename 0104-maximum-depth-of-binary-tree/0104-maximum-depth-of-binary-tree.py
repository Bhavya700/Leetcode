# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, root) -> int:
        if not root:
            return 0
        a=self.dfs(root.left)
        b=self.dfs(root.right)
        return 1+ max(a,b)

    