"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self,node:Optional['Node'])->Optional['Node']:
# https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode
        # t.c :- O(n)
        oldToNew={}
        def clone_recursive(node):
            if node in oldToNew:
                return oldToNew [node]
            copy = Node (node.val)
            #map original node to it's copy
            oldToNew[node] = copy
            #make copies of every neighbors of original node
            for nei in node.neighbors:
                copy.neighbors.append(clone_recursive(nei))
            return copy
        return clone_recursive(node) if node else None

# def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None
#         oldToNew = {}
#         queue=[node]

#         copy=Node(node.val)
#         oldToNew[node]=copy

#         while queue:
#             current= queue.pop(0)
#             for nei in current.neighbors:
#                 if nei not in oldToNew:
#                     n=Node(nei.val)
#                     oldToNew[nei]=n
#                     queue.append(nei)
#                 oldToNew[current].neighbors.append(oldToNew[nei])
        
#         return copy

        
