class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start,tmp):
            ans.append(tmp[:])
            for i in range(start,len(nums)):
                tmp.append(nums[i])
                backtrack(i+1,tmp)
                tmp.pop()
        backtrack(0,[])
        return ans
            