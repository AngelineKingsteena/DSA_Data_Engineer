class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ## video solution :- https://www.youtube.com/watch?v=iu0082c4HDE&ab_channel=NeetCode
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed ==
        n
        stack = [ ]
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
                