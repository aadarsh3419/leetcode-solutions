# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        queue = deque([(root,targetSum)])
        while queue:
            node,remaining = queue.popleft()
            remaining-=node.val
            if node.left is None and node.right is None:
                if remaining == 0:
                    return True
                continue
            
            if node.left:
                queue.append((node.left,remaining))
            if node.right:
                queue.append((node.right,remaining))

        return False

                

 

           