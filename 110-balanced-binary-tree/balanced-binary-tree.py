# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## video solution :-https://www.youtube.com/watch?v=QfJsau0ItOY&ab_channel=NeetCode
        ## A balanced binary tree or height-balanced binary tree is such a tree whose left and right subtree's height differ by not
        ## more than 1, which means the height difference could be -1, 0, and 1. A balanced binary tree is also known as a height-balanced tree.
        def dfs(root):
            if not root:
                ### return [balanced? bool,height] 
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            ### balanced = is left subtree balanced and right 
            ### subtree balanced and entire tree from root balanced
            balanced = (left[0] and right[0] and
            abs(left [1] - right [1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
        
        
