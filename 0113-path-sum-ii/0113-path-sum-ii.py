# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node,remaining,path):
            if node is None:
                return 
            path.append(node.val)
            remaining-=node.val
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])
            dfs(node.left,remaining,path)
            dfs(node.right,remaining,path)
            path.pop()
        dfs(root,targetSum,[])
        return result
        

            
        

