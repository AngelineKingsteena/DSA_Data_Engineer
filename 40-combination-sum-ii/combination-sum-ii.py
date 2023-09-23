class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort the candidates to handle duplicates
        candidates.sort()  
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # Include the current candidate
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Skip the current candidate
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res

# IF YOU WANT OUTPUT WITH DUPLICATES LIKE BELOW:-
# OUTPUT:-
# [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,5],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,5],[1,1,2,2,2],[1,1,6],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,5],[1,1,2,2,2],[1,1,6],[1,2,5],[1,7],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],[1,1,1,1,2,2],[1,1,1,5],[1,1,2,2,2],[1,1,6],[1,2,5],[1,7],[2,2,2,2],[2,6]]

# EXPECTED:- [[1,1,6],[1,2,5],[1,7],[2,6]]

#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()  # Sort the candidates to handle duplicates
#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
#             if i >= len(candidates) or total > target:
#                 return
#             # Include the current candidate
#             cur.append(candidates[i])
#             dfs(i, cur, total + candidates[i])
#             cur.pop()
#             # Skip the current candidate
#             dfs(i + 1, cur, total)
#         dfs(0, [], 0)
#         return res
        