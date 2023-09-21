# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # https://docs.google.com/document/d/1l9UDlLZeP0mQxExqjepsKbgYQj4nrNGUsyDlKDA1jyg/edit?usp=sharing
#         A path may or may not pass through the root.
# All paths = {all paths passing through a node and its desendants | for each node in tree}.
# Bottom-up DFS: from bottom to top,
# find the longest path passing through a node and its descendants,
# and updade the global longest path.

## for a trial run of [1,2,3,4,5]
## the recursion stack,goes to the botttommost left 4
## when at node val 4,the return is 1,so at node val 2,
## l_depth =1, and bcoz of node val 5, r_depth=1
        def depth(root):
            if not root:
                return 0
            l_depth = depth(root.left)
            r_depth = depth(root.right)
            ## diameter= depth(root.left) + depth(root.right)
            res[0] = max(res[0], l_depth + r_depth)
            ##max depth
            # # Adding 1 is the current node which is the 
            # parent of the two subtrees...bcoz in a empty 
            # tree,height is 0,whereas in a tree 
            ##with just 1 node height is 1
            return 1 + max(l_depth, r_depth)
        
        res = [0]
        depth(root)
        return res[0]
# Create a sample binary tree for testing
#         1
#        / \
#       2   3
#      / \
#     4   5
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# # Test the diameterOfBinaryTree function
# solution = Solution()
# diameter = solution.diameterOfBinaryTree(root)
# print("Diameter of the binary tree:", diameter)  # Expected output: 3

        