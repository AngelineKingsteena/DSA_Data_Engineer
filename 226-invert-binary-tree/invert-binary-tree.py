# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## video solution :-https://www.youtube.com/watch?v=OnSn2XEQ4MY&ab_channel=NeetCode
        if not root:
            return None
        # swap the children
        # tmp = root. left
        # root.left = root.right
        # root.right = tmp
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        