class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
# https://www.youtube.com/watch?v=B-QCq79-Vfw&ab_channel=NeetCode
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len (stones) > 1:
            first = heapq. heappop(stones)
            second = heapq. heappop (stones)
            if second > first:
                heapq. heappush (stones, first - second)
        stones.append(0)
        return abs(stones [0])   
        