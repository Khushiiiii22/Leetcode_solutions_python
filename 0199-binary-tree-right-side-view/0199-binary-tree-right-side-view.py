# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self,node,level,ans):
        if node is None:
            return
        if len(ans) == level:
            ans.append(node.val)

        if node.right:
            self.reverse(node.right,level+1,ans)
        if node.left:
            self.reverse(node.left,level+1,ans)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.reverse(root,0,ans)
        return ans
        