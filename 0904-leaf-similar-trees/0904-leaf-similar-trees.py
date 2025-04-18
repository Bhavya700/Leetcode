# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return True if self.dfs(root1)==self.dfs(root2) else False

    def dfs(self, root) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        return left+right
