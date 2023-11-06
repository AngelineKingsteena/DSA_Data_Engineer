class Solution:
    # https://www.youtube.com/watch?v=s8p8ukTyA2I&ab_channel=NeetCode
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     # each task 1 unit time
    #     # minimize idle time
    #     count = Counter (tasks)
    #     maxHeap = [-cnt for cnt in count.values ()]
    #     heapq. heapify(maxHeap)
    #     time = 0
    #     q = deque () # pairs of [-cnt, idleTime]
    #     while maxHeap or q:
    #         time += 1
    #         if maxHeap:
    #             cnt = 1 + heapq. heappop (maxHeap)
    #             if cnt:
    #                 q.append([cnt, time + n])
    #         if q and q[0][1] == time:
    #             heapq. heappush (maxHeap, q.popleft ()[0])
    #     return time
        

        def leastInterval(self, tasks: List[str], n: int) -> int:
            if n == 0: return len(tasks)
            counter = collections.Counter(tasks)
            maxCount = 0
            maxValue = max(counter.values())
            for cha, val in counter.items():
                if val == maxValue:
                    maxCount += 1
            return max((n + 1) * (maxValue - 1) + maxCount ,len(tasks))

# The last part is tricky to understand:

# OGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1
        
        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
                                     # ans   =     rows_except_last   * columns +        last_row
            
            
        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)


# Assume 3 cases
# Case 1) if there is a one task occurring more than remaining ones: in this case its definite that all time will taken because of that one task, other tasks would just be placed in buffer space.

#     eg: ('A','A','A','B','B'), n = 2
#     3 A's and 2 B's, then  max_value= 3 and only 1 task will be max.
#     Therefore
#     (max_value - 1) * (n + 1) + letters_having_max_value = (3-1)*3 + 1 = 7
#     i.e  A _ _ A _ _ A
#     Other tasks will just fill up the buffer space
# Case 2) if there are two maximum's:
# i.e('A','A','A','B','B','B'), n=2
# this one is a clear case because either
# A _ _ A _ _ A B or B _ _ B _ _ B A
# it will require max_value - 1 buffers and the last characters would be both maximum tasks i.e
# letters_having_max_value

#     (max_value - 1) * (n + 1) + letters_having_max_value = (3-1)*3 + 2 = 8
# Case 3) maximum character repeating is less than half :

#     ('A','A','B','C','D','E'), n=2

#     (max_value - 1) * (n + 1) + letters_having_max_value = (2-1)*3 + 1 = 4
#     But there are six tasks and would require at least 6 unit of time.
#     thus max(4, len(tasks))