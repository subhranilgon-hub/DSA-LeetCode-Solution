class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dict1=[[1]]
        for i in range(numRows -1):
            temp=[0]+dict1[-1]+[0]
            curr=[]
            for j in range(len(dict1[-1])+1):
                curr.append(temp[j]+temp[j+1])
            dict1.append(curr)
        return dict1