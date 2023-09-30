class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        # The time complexity of the code is O(m * n), where:
# m is the number of rows in the input matrix A.
# n is the number of columns in the input matrix A.
        # The space complexity of the code is O(m * n), which is the space required for the ans list to store the output.
        row=len(A)
        ans=[]
        if ((row==0) or (A==None)):
            return []
        else: 
            col=len(A[0])
        
        direc=0
        top,left=0,0
        bottom,right=row-1,col-1
        
        while((top<=bottom) and (left<=right)):
            if direc==0:
                for i in range(left,right+1):
                    ans.append(A[top][i])
                top+=1
                direc=1
            elif direc==1:
                for i in range(top,bottom+1):
                    ans.append(A[i][right])
                right-=1
                direc=2
            elif direc==2:
                for i in range(right,left-1,-1):
                    ans.append(A[bottom][i])
                bottom-=1
                direc=3
            elif direc==3:
                for i in range(bottom,top-1,-1):
                    ans.append(A[i][left])
                left+=1
                direc=0
        return ans

        