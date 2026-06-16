# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def dfs(node):
            if node is None:
                data.append("N")
                return None
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return data

        dfs(root)
        print(data)
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            curr = data[i]
            i+=1
            if curr == "N":
                return None
            root = TreeNode(int(curr))
            root.left =  dfs()
            root.right = dfs()
            
            return root
            
        return dfs()
        
   
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))