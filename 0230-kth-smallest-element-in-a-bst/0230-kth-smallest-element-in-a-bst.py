# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. Backtrack: curr is now None, so pop from stack
            curr = stack.pop()
            c +=1
            if c==k:
                return curr.val
            # 3. We've visited the node and its left subtree; now move right
            curr = curr.right

            
        return -1
        