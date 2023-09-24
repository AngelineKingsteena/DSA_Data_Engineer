class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
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

        