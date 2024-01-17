class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
# https://www.youtube.com/watch?v=kShkQLQZ9K4&ab_channel=NeetCode
        ## need to use set only,coz in triplets=[[4,5,2],[4,2,7],[5,8,6],[3,6,6],[4,5,2]],target=[4,5,7]
        ## goal becomes [0, 1, 0, 2, 0, 1] instead of [0,1,2]
        good = set ( )
        for t in triplets:
           ## ignore the triplet which has ith element greater than ith element
           ## in target,even if one index value is greater,completely ignore full triplet
            ## example expected=False for eg: triplets = [[3,5,1],[10,5,7]],target =[3,5,7]
            ## in eg target can't be formed coz 2nd triplet is completely ignore coz 10 > target's 3 at 0th index
            if t[0] > target[0] or t[1] > target[1] or t[2] > target [2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    ## important to add indice rather than value,coz target might have duplicates
                    ## like in triplets=[[2,5,3],[2,3,4],[1,2,5],[5,2,3]],target=[5,5,5]
                    good.add(i)
        return len (good) == 3
                
