class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort the candidates to handle duplicates
        candidates.sort()  
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    # Skip duplicates to avoid duplicates 
                    # in the result
                    continue  
                if total + candidates[j] <= target:
                    cur.append(candidates[j])
                    # Use j + 1 to avoid reusing the same number
                    # WITHOUT J+1
                    # candidates =[10,1,2,7,6,1,5]
                    # target =8
                    # Output
                    # [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,2],
                    # [1,1,1,1,2,2],[1,1,1,5],[1,1,2,2,2],[1,1,6],
                    # [1,2,5],[1,7],[2,2,2,2],[2,6]]
                    # Expected
                    # [[1,1,6],[1,2,5],[1,7],[2,6]]
                    dfs(j+1, cur, total + candidates[j])
                    cur.pop()
        dfs(0, [], 0)
        return res
        