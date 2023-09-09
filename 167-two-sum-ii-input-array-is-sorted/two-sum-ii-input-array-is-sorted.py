class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #video solution:-https://www.youtube.com/watch?v=cQ1Oz4ckceM&ab_channel=NeetCode
        # l, r = 0, len (numbers) - 1
        # while l < r:
        #     cursum = numbers [l] + numbers [r]
        #     if cursum > target:
        #         r -= 1
        #     elif cursum < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        # return []
        seen={}
        for ind,value in enumerate(numbers):
            rem=target-value
            if rem in seen:
                return [min(ind,numbers.index(rem))+1,max(ind,seen[rem])+1]
            seen[value]=ind
        return []
            