class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        # sorted and reversed coz, the car closeest to destination will anyway block the rest of the cars behind it to maybe form a fleet,if they catch up
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order,BCOZ OF WHICH FIRST ELEMENT(TIME) ADDED IN STACK IS ALREADY LESSER
            ## SO IF EVEN LESSER VALUE [-1] COMES POP IT OUT
            stack.append((target - p) / s) # time taken
            # the car which is coming behind (stack[-2])  takes more time (indirectly is slower )
            ## than closest car,so will become a fleet with recent closest (stack[-1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                ### remove the lesser time car
                stack.pop()
            ## basically keep storing cars in ascending order of time taken in stack ,also keep poppinf,if better component comes up
        return len(stack)
        
