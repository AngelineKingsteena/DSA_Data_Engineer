# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ## video solution :- https://www.youtube.com/watch?v=Hr5cWUld4vU&ab_channel=NeetCode
        res = [root.val]
        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root. left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum WITH split
            res[0] = max(res [0], root.val + leftMax + rightMax)
            # compute max path sum WITHOUT split
            return root. val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5

    #     IN SUBTREE  3   path sum WITH split is either 7 0r 8,but max is 8,
    #                / \   so max path sum WITH split is 8
    #               4   5

    # so total max path sum WITHOUT split will be  1+above computed 8

    #     1                            
    #      \
    #       3
    #        \
    #         5

        