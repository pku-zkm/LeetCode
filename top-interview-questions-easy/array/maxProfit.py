class Solution:
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     n = len(prices)
    #     if n<=0:
    #         return 0
    #     mat = []
    #     for i in range(n):
    #         mat.append([0]*n)
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             for k in range(i, j):
    #                 if prices[j]-prices[k] > mat[i][j]:
    #                     mat[i][j] = prices[j]-prices[k]
    #     rec = [0]*n
    #     for i in range(n):
    #         m = mat[0][i]
    #         for j in range(1,i):
    #             if rec[j-1]+mat[j][i] > m:
    #                 m = rec[j-1]+mat[j][i]
    #         rec[i] = m
    #     return max(rec)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<1:
            return 0
        s=0
        i,j=0,0
        while i<n and j<n:
            while i+1<n and prices[i+1]<prices[i]:
                i+=1
            j=i
            while j+1<n and prices[j+1]>prices[j]:
                j+=1
            s+=prices[j]-prices[i]
            i=j+1
        return s












        

        

s=Solution()
m=s.maxProfit([7,1,5,3,6,4])
print(m)