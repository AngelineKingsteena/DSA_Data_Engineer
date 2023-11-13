class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #https://www.youtube.com/watch?v=rI2EBUEMfTk&ab_channel=NeetCode
        minheap,res=[],[]
        for x,y in points:
            dist=x**2+y**2
            heapq.heappush(minheap,(dist,(x,y)))
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        
