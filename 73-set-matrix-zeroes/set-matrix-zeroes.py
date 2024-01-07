class Solution:
    """
1)FLAG EXISTENCE OF ZERO IN OUTER PERIPHERAL:iterate over rows,see if any
element in 0,column is 0,update,firstcol=True
2)FLAG EXISTENCE OF ZERO IN OUTER PERIPHERAL:iterate over columns,see
if any elemnt in 0,row is 0,update firstrow=True
3)FLAG EXISTENCE OF ZERO IN INNER PERIPHERAL:iterate through rows and 
columns from 0 index,if any 1 elemnt[i][j] is 0,set entire row [i][0]
and entire column[j][0]=0
4)BASED ON FLAGS CHANGE VALUES(FROM ALL rows and columns EXCEPT FIRST
ROW AND FIRST COLUMN) INTO 0:-iterate through ALL rows and columns EXCEPT 
FIRST ROW AND FIRST COLUMN I.E from index1,if [i][0] or [0][j]==0,set [i][j]=0
5)BASED ON FLAGS CHANGE VALUES FROM FIRST COLUMNS INTO 0:-if firstcol=True
,iterate through rows and set entire col=0,i.e,[i][0]=0
6)BASED ON FLAGS CHANGE VALUES FROM FIRST ROW INTO 0:-if firstrow=True,
iterate through cols and set entire row=0,i.e,[0][j]=0

"""
    def setZeroes(self,A):
        firstRow = False
        firstCol = False
        row=len(A)
        col=len(A[0])
        
        #1)
        for i in range(row):
            if A[i][0]==0:
                firstCol=True
                break
        #2)
        for i in range(col):
            if A[0][i]==0:
                firstRow=True
                break
        
        #3)
        for i in range(row):
            for j in range(col):
                ## 0 found inside
                if A[i][j]==0:
                    ## flag it outside
                    A[i][0]=0
                    A[0][j]=0
        
        #4)
        for i in range(1,row): ## 1 bcoz,to not disturb flag
            for j in range(1,col): ## 1 bcoz,to not disturb flag
                ## based on outer flag
                if ((A[i][0]==0) or (A[0][j]==0)):
                    ## set 0's inside
                    A[i][j]=0
        #5)
        if firstRow:
            for i in range(col):
                A[0][i]=0
        
        #6)
        if firstCol:
            for i in range(row):
                A[i][0]=0
        
        return A
