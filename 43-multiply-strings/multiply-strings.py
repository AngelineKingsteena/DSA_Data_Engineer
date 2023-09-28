class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strint(n):
            result=0
            for i in range(len(n)):
                result = result*10 + ord(n[i])-ord('0')
            return result
        return str(strint(num1)*strint(num2))
    