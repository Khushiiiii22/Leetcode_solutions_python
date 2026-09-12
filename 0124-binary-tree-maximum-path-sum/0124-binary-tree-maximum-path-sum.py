# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def solve(node):
            nonlocal maxi
            if node == None:
                return 0
            ls = solve(node.left)
            if ls<0:
                ls = 0
            rs = solve(node.right)
            if rs<0:
                rs = 0
            maxi = max(maxi,ls+node.val+rs)
            return node.val+max(ls,rs)
        solve(root)
        return maxi
        