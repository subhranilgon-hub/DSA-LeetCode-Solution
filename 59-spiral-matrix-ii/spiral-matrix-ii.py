class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for  i in range(n)]

        total=n*n
        c=0
        curr_val=1

        colstart=0
        rowstart=0
        colend=n-1
        rowend=n-1

        while c<total:
            #rowstart, colstart-> colend
            for i in range(colstart, colend+1):
                matrix[rowstart][i]=curr_val
                curr_val+=1
                c+=1
            rowstart+=1

            if c==total:
                break

            #colend ,rowstart-> rowend
            for i in range(rowstart, rowend+1):
                matrix[i][colend]=curr_val
                curr_val+=1
                c+=1
            colend-=1

            if c==total:
                break

            #rowend, colend->colstart
            for i in range(colend, colstart-1,-1):
                matrix[rowend][i]=curr_val
                curr_val+=1
                c+=1
            rowend-=1

            if c ==total:
                break

            #colstart, rowend->rowstart

            for i in range(rowend, rowstart-1,-1):
                matrix[i][colstart]=curr_val
                curr_val+=1
                c+=1
            colstart+=1

        return matrix




        
        