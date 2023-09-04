class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ## video solution :-https://www.youtube.com/watch?v=iu0082c4HDE&ab_channel=NeetCode
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop ())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int (c))
        return stack[0]
        