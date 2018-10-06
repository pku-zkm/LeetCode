class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        nc=n//2
        for i in range(nc):
            d=n-i-1
            for j in range(d):
                x,y=i,i+j
                for k in range(4):
                    a=matrix[x][y]
                    if y+d<n:
                        b=matrix[x][y+d]
                        matrix[x][y+d]=a
                        a=b
                        x,y=x,y+d
                    elif x+d<n:
                        b=matrix[x+d][y]
                        matrix[x+d][y]=a
                        a=b
                        x,y=x+d,y
                    elif 


