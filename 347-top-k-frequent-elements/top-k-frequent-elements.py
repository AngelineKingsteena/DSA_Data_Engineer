import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        # -v becoz in the tuple,the first count to pop out should be the negatively least aka positively great regardless  of actual number
        # example in Counter([7,1,1,1,1,7,7,7,7,6,6,6,6,6,6,-9,-8]) #Counter({7: 5, 1: 4, 6: 6, -9: 1, -8: 1})
        # if we start popping w/o -v,we get (1,-9) first
        # but if we start popping with -v,we get (-7,5)
        # becoz in a tuple ,heap first sorts in order of 1,2..nth element,
        # so when if we use -v,it comes to (-1,-9) and (-1,8) and (-7,5),
        # and if we pop,it'll pop (-7,5),(-1,-9),(-1,-8) in order
        c = [(-v,k)for k,v in c.items()] 
        heapq.heapify(c)
        output=[]
        for i in range(k):
            item= heapq.heappop(c)
            output.append(item[1])
        return output