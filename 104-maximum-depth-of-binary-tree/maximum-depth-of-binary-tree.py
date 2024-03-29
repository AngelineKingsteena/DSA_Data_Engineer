# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=hTM3phVI6YQ&ab_channel=NeetCode

        ####### recursive
        if not root:
            return 0
        # Adding 1 is the current node which is the parent of the two subtrees...bcoz in a empty tree,height is 0,whereas in a tree 
        #with just 1 node height is 1
        ## This solution has a time complexity of O(n), where n is the number of nodes in the binary tree, since we visit each node exactly once. The space complexity is O(h), where h is the height of the binary tree, since the recursive call stack can have at most h frames.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        # ##### bfs or level order traversal
        # if not root:
        #     return 0
        # level = 0
        # q = deque ( [root ])
        # while q:
        #     for i in range (len (q)) :
        #         node = q .popleft ()
        #         if node. left:
        #             q. append (node. left)
        #         if node.right:
        #             q.append (node. right)
        #     level += 1
        # return level

        # ## DFS PREDORDER

        # stack = [[root, 1]]
        # res = 0
        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        # return res

        
        
