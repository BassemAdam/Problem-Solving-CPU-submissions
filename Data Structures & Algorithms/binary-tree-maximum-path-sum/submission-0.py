# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        self.maxSum = float('-inf')
        
        def getOpt(root):
            if not root: return 0
            
            leftSum =  getOpt(root.left)
            rightSum = getOpt(root.right)

            pathSum = root.val +  max(leftSum,rightSum)

            self.maxSum = max(
                self.maxSum,
                root.val + leftSum + rightSum
            )

            return max(pathSum,0)
          

        getOpt(root)
        return self.maxSum
