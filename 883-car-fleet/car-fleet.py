class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        # sorted and reversed coz, the car closeest to destination will anyway block the rest of the cars behind it to maybe form a fleet,if they catch up
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p) / s) # time taken
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                ### remove the lesser time car
                stack.pop()
        return len(stack)
        