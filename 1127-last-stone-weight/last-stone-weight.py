class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
# https://www.youtube.com/watch?v=B-QCq79-Vfw&ab_channel=NeetCode
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len (stones) > 1:
            first = heapq. heappop(stones)
            second = heapq. heappop (stones)
            if second > first:
                heapq. heappush (stones, first - second) # if append (1) instead of (-1)
        stones.append(0) ## finaly it'd be [-1,0]
        return abs(stones [0])   
        
