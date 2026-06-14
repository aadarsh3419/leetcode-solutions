    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,remaining):
            if node is None:
                return False
            remaining -= node.val
            if not node.left and not node.right:
                return remaining == 0
            return dfs(node.left,remaining) or dfs(node.right,remaining)
        return dfs(root,targetSum)
        
        

    

            