from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=[]
        def bfs(node):
            nonlocal level
            q=deque()
            if node:
                q.append(node)
            while len(q)>0:
                b=[]
                for i in range(len(q)):
                    curr=q.popleft()
                    b.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                level.append(b)
        bfs(root)
        return level
