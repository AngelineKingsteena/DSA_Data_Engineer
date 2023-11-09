class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # https://www.youtube.com/watch?v=amnrMCVd2YI&ab_channel=NeetCode
        # T.C :- Nlog(N)
        if len(hand) % groupSize:
            return False
        # counter can also be used
        count = {}
        for n in hand:
            count [n] = 1 + count.get (n, 0)

        minH = list(count.keys ())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                # in eg counter {1:1,3:1} first=1
                if i not in count:
                    ,#so when i =2
                    return False
                count[i] -= 1
                if count [i] == 0:
                    if i != minH[0]:
                        return False
                    heapq. heappop (minH)
        return True
                
