# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## video solution :-https://www.youtube.com/watch?v=QfJsau0ItOY&ab_channel=NeetCode
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
        
        