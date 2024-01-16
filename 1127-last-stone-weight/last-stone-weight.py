class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
# https://www.youtube.com/watch?v=B-QCq79-Vfw&ab_channel=NeetCode
        ## to implement max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len (stones) > 1:
            first = abs(heapq. heappop(stones))
            second = abs(heapq. heappop (stones))
            if second < first:
                heapq. heappush (stones, -(first - second))
        # edge case:- incase no stone left
        stones.append(0) ##in case stones =[2,2]
        return abs(stones [0])   
        