# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root == q : return root

        # go search left for p and q
        foundleft = self.lowestCommonAncestor(root.left,p,q)
        # go search right for p and q
        foundright = self.lowestCommonAncestor(root.right,p,q)

        # once you found p and q
        if foundright and foundleft:
           return root

        return foundleft if foundleft else foundright