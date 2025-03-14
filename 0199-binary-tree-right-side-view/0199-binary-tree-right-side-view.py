# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        ans=[]
        while len(queue) > 0:
            c=[]
            for i in range(len(queue)):
                curr = queue.popleft()
                c.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            print(c)
            ans.append(c[0])
            level += 1

        return ans
