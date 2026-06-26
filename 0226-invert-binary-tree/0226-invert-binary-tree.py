# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])
        while queue:
            p = queue.popleft()
            p.left,p.right = p.right,p.left
            if  p.left:
                queue.append(p.left)
            if  p.right:
                queue.append(p.right)
        return root



        
        