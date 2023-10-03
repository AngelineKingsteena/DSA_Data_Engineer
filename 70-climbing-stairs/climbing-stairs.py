class Solution:
    def climbStairs(self, n: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode
        ## s.c :-
        ## t.c :-n
        #[newOne,newTwo/oldOne,oldTwo]
        #[1+1,1,1]
        one, two = 1, 1 #two is no. of steps to reach top from top
         #two is no. of steps to reach top from top before step
        ## skip last two
        for i in range(n - 1):
            # temp = one
            # one = one + two
            # two = temp
            one,two=one + two,one
        return one
        