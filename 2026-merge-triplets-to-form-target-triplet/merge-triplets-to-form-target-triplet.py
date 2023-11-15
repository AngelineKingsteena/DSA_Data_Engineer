class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
# https://www.youtube.com/watch?v=kShkQLQZ9K4&ab_channel=NeetCode
        ## need to use set only,coz in triplets=[[4,5,2],[4,2,7],[5,8,6],[3,6,6],[4,5,2]],target=[4,5,7]
        ## goal becomes [0, 1, 0, 2, 0, 1] instead of [0,1,2]
        good = set ( )
        for t in triplets:
            ## because the target's ith value has to be max of all the ith values of all triplets
            ## so if ith value of triplet is greater,target cant be having max
            if t[0] > target[0] or t[1] > target[1] or t[2] > target [2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    ## important to add indice rather than value,coz target might have duplicates
                    ## like in triplets=[[2,5,3],[2,3,4],[1,2,5],[5,2,3]],target=[5,5,5]
                    good.add(i)
        return len (good) == 3
                
