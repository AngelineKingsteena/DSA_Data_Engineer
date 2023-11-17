class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=deque()
        q.append((beginWord,1))
        while q:
            word,step=q.popleft()
            for i in range(len(beginWord)):
                for j in range(26):
                    new=word[:i]+chr(97+j)+word[i+1:] ## or chr(ord('a')+j)
                    if new==endWord:
                        return step+1
                    if new in wordList:
                        q.append((new,step+1))
                        ## in test case like:-beginWord = "hot",endWord ="dog",wordList =["hot","dog"],Expected=0 to avoid loop
                        wordList.remove(new)
        return 0
        
