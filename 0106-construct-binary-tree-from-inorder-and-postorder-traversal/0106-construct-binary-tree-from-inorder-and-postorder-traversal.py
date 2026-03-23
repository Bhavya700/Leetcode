# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, start=None, end=None):
#         self.val = val
#         self.start = start
#         self.end = end
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx,val in enumerate(inorder)}
        self.index = len(postorder)-1
        def helper(start,end):
            if start > end:
                return None
            
            root_val = postorder[self.index]
            self.index -= 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            root.right = helper(mid+1,end)
            root.left = helper(start,mid-1)

            return root
        return helper(0,len(inorder)-1)
