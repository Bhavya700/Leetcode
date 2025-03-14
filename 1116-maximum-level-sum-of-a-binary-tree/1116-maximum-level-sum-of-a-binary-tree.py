from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        if not root:
            return 0
        queue.append(root)
        level=1
        val=root.val
        ans=1
        while len(queue)>0:
            s=0
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    s+=curr.left.val
                    queue.append(curr.left)
                if curr.right:
                    s+=curr.right.val
                    queue.append(curr.right)
            level+=1
            if s>val and len(queue)>0:
                val=s
                ans=level
        return ans