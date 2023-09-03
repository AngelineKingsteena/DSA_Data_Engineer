class Solution:
   def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
        ###In each iteration check if required number (required  number = target sum - current number) is
        ###present in the hashmap.

        ###If present, return {required number index, current number index} as  result.

        ###Otherwise add the current iteration number as key and its index as value to the hashmap.
        ###Repeat this  until you find the result.

            if remaining in seen:
                # print(i,value,remaining)
                return [min(i,nums.index(remaining)), max(i,seen[remaining])] #4,8 (earliest)
    #             return [i+1, seen[remaining]+1]  # [8,6]  latest

            seen[value] = i
        return []

#twoSum([ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ],-3)