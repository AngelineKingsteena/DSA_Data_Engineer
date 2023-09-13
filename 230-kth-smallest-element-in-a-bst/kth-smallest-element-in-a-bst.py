# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode
        ## since its a bst,solution can be found by doing inorder traversal --> L,N,R
        stack = []
        trav = root
        count = 0
        while trav or stack:
            if trav:
                stack.append(trav)
                trav = trav.left
            else:
                ## get the parent
                u = stack.pop()
                count += 1
                if count == k:
                    return u.val
                ## and start doing inorder travsersal of parent
                trav = u.right
