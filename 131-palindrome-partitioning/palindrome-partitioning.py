class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ## video solution :- https://www.youtube.com/watch?v=xhEEpnn0x1U&ab_channel=TimothyHChang
        ## s.c :-
        ## t.c :-2^n


        n= len(s)
        output = []
        def dfs(st,sofar):
            #base case
            if st==n:
                output.append(sofar)
            for i in range(st,n):
                if s[st:i+1]==s[st:i+1][::-1]: #is palindrome?
                    dfs(i+1, sofar+[s[st:i+1]])
        dfs(0, [])
        return output

###### recursion tree explanation
    #              aab
    #             /
    #            /  aa -> aab->None
    #           / ↗ |  ↖
    #          a↗   b->None
    #         /    [aa,b] = sofar
    #        /  
    #       a ->ab->None   
    #      /  ↖
    #     b->None
    #  [a,a,b] = sofar

    # basically create new func stack only if its palindrome,
    # else return None and pop back from stack