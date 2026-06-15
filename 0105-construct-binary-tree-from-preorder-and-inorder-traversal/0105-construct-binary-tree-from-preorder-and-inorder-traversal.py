# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        tree = {}
        for i in range(n):
            tree[inorder[i]] = i
        def helper(pre_left,pre_right,in_left,in_right):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            idx = tree[root_val]
            root = TreeNode(root_val)
            left_size = idx - in_left

            root.left = helper(pre_left+1,pre_left + left_size,in_left,idx-1)
            root.right = helper(pre_left+left_size + 1,pre_right,idx+1,in_right)

            return root
        return helper(0,len(preorder)-1,0,n-1)
            
        

