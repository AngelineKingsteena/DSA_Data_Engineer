class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start, tmp):
            if start == len(nums):
                ans.append(tmp[:])
                return
            # Include the current element
            tmp.append(nums[start])
            backtrack(start + 1, tmp)
            tmp.pop()
            # Skip the current element
            backtrack(start + 1, tmp)
        backtrack(0, [])
        return ans




            