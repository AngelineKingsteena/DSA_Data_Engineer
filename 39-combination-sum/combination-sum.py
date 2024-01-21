class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # Include the current candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop() # or cur.remove(candidates[i])
            # Skip the current candidate
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res

#                                             (i=0, cur=[], total=0)
#                                             /                   \
#                      (i=0, cur=[2], total=2)                    (i=1, cur=[], total=0)
#                     /                   \                                   \
# (i=0, cur=[2, 2], total=4)   (i=1, cur=[2], total=2)                     (i=1, cur=[3], total=3)
#           /                   \                       \                           \
# (i=0, cur=[2, 2, 2], total=6)  (i=1, cur=[2, 3], total=5)                  (i=1, cur=[3, 3], total=6)
#           \                   /                                               /
# (i=0, cur=[2, 2, 2, 2], total=8)                                        (i=2, cur=[3, 3, 7], total=13)
#           /                   \
# (i=0, cur=[2, 2, 2, 2, 2], total=10)

        
