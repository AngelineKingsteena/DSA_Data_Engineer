class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ## video solution :- https://www.youtube.com/watch?v=0snEunUacZY&ab_channel=NeetCode
        ## s.c :-
        ## t.c :- n(4^ n)  where n =len(i/p string)
        res = []
        digitToChar = { "2": "abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",
        "8":"tuv","9":"wxyz"}
        def backtrack(i, curStr):
            if len(curStr) == len (digits) :
                res.append (curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res

# ############
#       a                b
#      /               ↗ |
#     /               /  |      etc
#    d  e     f      /   d
# [ad]↗ [ae]↗ [af] ⤴  [bd] 
#  ↪None ↪None   ↪None  ↪None     