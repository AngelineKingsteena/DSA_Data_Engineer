class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strint(n):
            ##convert num1 and num2 strings into int
            result=0
            for i in range(len(n)):
                ## convert"22" into int by 2*10+2
                result = result*10 + ord(n[i])-ord('0')
            return result
        return str(strint(num1)*strint(num2))
    