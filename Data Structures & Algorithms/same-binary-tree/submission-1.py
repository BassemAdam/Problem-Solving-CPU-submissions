# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def dfs(t,arr):
            if t is None:
                arr.append(None)
                return

            dfs(t.left,arr)
            arr.append(t.val)
            dfs(t.right,arr)
            arr.append(t.val)
        dfs(p,arr1)
        dfs(q,arr2)
        print(arr1)
        print(arr2)
        return arr1 == arr2
