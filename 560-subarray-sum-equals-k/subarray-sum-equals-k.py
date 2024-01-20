class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## ecplanation https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode
        ## t.c o(n)
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 } 
        ## key: sum that can be chopped off,values: count of occurences
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums [curSum] = 1 + prefixSums.get (curSum, 0)
        return res