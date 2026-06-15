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
        def helpe(where_p,end_p,where_i,end_i):
            if where_p > end_p:
                return None
            value_root = preorder[where_p]
            root = TreeNode(value_root)
            idx  = tree[value_root]
            size_of_left = idx - where_i
            root.left = helpe(where_p+1,where_p+size_of_left,where_i,idx-1)
            root.right =helpe(where_p+size_of_left+1,end_p,idx+1,end_i)
            return root
        return helpe(0,len(preorder)-1,0,n-1)
