# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## video solution :-  https://www.youtube.com/watch?v=ihj4IQGZ2zc&ab_channel=NeetCode

        # PREorder traversal --> N,L,R (so first val is always root)
        # inorder traversal --> L,N,R (from here we know the 
        # left and right subtree using root found from preorder)

        if not preorder or not inorder:
            return None
        root = TreeNode (preorder [0])
        mid = inorder.index(preorder [0])
        ### preorder[1:mid + 1] and not preorder[0:mid + 1] 
        # since 0 is root
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder [mid + 1:], inorder [mid + 1:])
        return root
        