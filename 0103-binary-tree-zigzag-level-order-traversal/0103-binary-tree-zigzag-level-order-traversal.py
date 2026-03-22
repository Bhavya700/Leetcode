# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
    
            res[level].append(node.val)
            
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, 0)
        for i in range(1,len(res),2):
            res[i]=res[i][::-1]
        return res
