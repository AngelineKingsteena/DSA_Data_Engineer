# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode
        stack = []
        trav = root
        count = 0
        while trav or stack:
            if trav:
                stack.append(trav)
                trav = trav.left
            else:
                u = stack.pop()
                count += 1
                if count == k:
                    return u.val
                trav = u.right
