# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ## idea is for each left subtree,check if node's val is statifying boundary
        ## -inf<val<subtree's root and
        # for each right subtree,check if node's val is statifying boundary
        ## subtree's root<val<inf and
        ## video solution :- https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            ## valid(node.left, left, node.val) = every values in the left
            #  subtree(node.left) has to be lesser than parent(node.val)
            ## and greater than max (oldest ancestor aka root , inf)
            return (valid(node.left, left, node.val) and
            valid(node .right, node.val, right))
        return valid(root, float ("-inf"), float ("inf"))

#                5  (-inf<5<inf)
#               / \
# (-inf<3<5)   3   7  (5<7<inf)
#                 / \
#      (5<4<7)   4   8 ( 7<8<inf)

#  (5<4<7)  this breaks,so above dia is not valid bst
           