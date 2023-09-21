# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # https://docs.google.com/document/d/1l9UDlLZeP0mQxExqjepsKbgYQj4nrNGUsyDlKDA1jyg/edit?usp=sharing
# This solution has a time complexity of O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once. The space complexity is O(h), where h is the height of the binary tree, since the recursive call stack can have at most h frames.

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

        