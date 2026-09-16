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
        self.encode = []
        def dfs(root):
            if not root:
                self.encode.append('?')
                self.encode.append(',')
                return None
            self.encode.append(root.val)
            self.encode.append(',')
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ''.join(map(str,self.encode))
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def parse_chr(data):
            for token in data.split(','):
                if not token:
                    continue
                yield None if token == '?' else int(token)
        
        self.encode1 = list(parse_chr(data))
        # value then go get its children starting with left then right
        self.ptr = 0
        def dfs(arr):
            if self.ptr >= len(arr): return

            if arr[self.ptr] == None: 
                self.ptr +=1
                return

            root = TreeNode(arr[self.ptr])
            self.ptr +=1

            root.left = dfs(arr)
            root.right = dfs(arr)

            return root
        return dfs(self.encode1)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))