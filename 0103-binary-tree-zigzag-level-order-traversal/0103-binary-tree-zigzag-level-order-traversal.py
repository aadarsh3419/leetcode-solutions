# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arry = []
        if root is None:
            return arry
        le = 0
        queue = deque([(root)])
        while queue:
            lev = len(queue)
           
            level = []
            for _ in range(lev):
                node = queue.popleft()
                level.append(node.val)
               
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if le % 2==0:
                level = level[::-1]
            arry.append(level)
            le+=1
        return arry