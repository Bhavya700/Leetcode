# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(node, prev_dir, curr_len):
            nonlocal max_len
            max_len = max(curr_len, max_len)
            if node.left: 
                if prev_dir == "right":
                    dfs(node.left, "left", curr_len + 1)
                else:
                    dfs(node.left, "left", 1)
            if node.right: 
                if prev_dir == "left":
                    dfs(node.right, "right", curr_len + 1)
                else:
                    dfs(node.right, "right", 1)
            
        dfs(root, '', 0)

        return max_len
            
    