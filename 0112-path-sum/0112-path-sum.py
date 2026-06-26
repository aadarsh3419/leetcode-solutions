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
        targetSum -= root.val
        queue = deque([(root,targetSum)])
        while queue:
            node,remaining = queue.popleft()
            
            if node.left is None and node.right is None and remaining==0:
                return True
            if node.left:
                lr = remaining-node.left.val
                queue.append((node.left,lr))
            if node.right:
                rr=remaining-node.right.val
                queue.append((node.right,rr))
            
        return False
         

