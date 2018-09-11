class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            nums[i]=2*nums[i]+1
        s=sum(nums)
        for i in range(n):
            x=(s-nums[i])//2
            y=(s-nums[i])%2
            if y==0 and 
                return (nums[i]-1)//2

s=Solution()
print(s.singleNumber( [4,1,2,1,2]))