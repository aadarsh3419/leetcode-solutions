# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        tree = {}
        for i in range(n):
            tree[inorder[i]] = i
        
        def helpe(ps,pe,ist,ie):
            if  ps > pe:
                return None
            rv = postorder[pe]
            idx = tree[rv]
            root = TreeNode(rv)
            ls = idx - ist
            rs = ie-idx 
            root.right = helpe(ps+ls,pe-1,idx+1,ie)
            root.left = helpe(ps,ps+ls-1,ist,idx-1)
            return root
        return helpe(0,n-1,0,n-1)


            