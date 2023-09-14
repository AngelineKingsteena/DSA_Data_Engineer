class Solution:
    def climbStairs(self, n: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode
        ## s.c :-
        ## t.c :-
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
        