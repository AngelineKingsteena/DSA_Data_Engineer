# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ## video solution :- https://www.youtube.com/watch?v=6ZnyEApgFYg&ab_channel=NeetCode
        res = []
        q = collections. deque ()
        q. append (root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen) :
                node = q.popleft ()
                if node:
                    level.append (node.val)
                    q. append (node. left)
                    q.append (node.right)
            if level:
                res. append(level)
        return res

# # Create the binary tree for testing
# #         3
# #        / \
# #       9  20
# #          / \
# #         15  7
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# # Test the levelOrder function
# solution = Solution()
# result = solution.levelOrder(root)
# print(result)  # Expected output: [[3], [9, 20], [15, 7]]