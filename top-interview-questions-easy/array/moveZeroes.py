class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        n=len(nums)
        while i<n and j<n:
            while i<n and nums[i]!=0:
                i+=1
            j=i+1
            while j<n and nums[j]==0:
                j+=1
            if j>=n:break
            nums[i]=nums[j]
            nums[j]=0
            i+=1
    