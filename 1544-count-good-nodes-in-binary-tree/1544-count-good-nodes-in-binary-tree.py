# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self,root, m)->int:
        if not root:
            return 0
        good = 1 if root.val>=m else 0
        m=max(m,root.val)
        left=self.dfs(root.left, m)
        right=self.dfs(root.right, m)
        return good+left+right
