class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
# https://www.youtube.com/watch?v=kShkQLQZ9K4&ab_channel=NeetCode
        good = set ( )
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target [2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len (good) == 3
                