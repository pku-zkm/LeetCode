class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            x=nums.pop()
            nums.insert(0,x)
    
    def rotate2(self, nums, k):
        n=len(nums)
        k=k%n
        

s=Solution()
nums=[1,2,3,4,5,6,7]
k=3
s.rotate(nums,k)
print(nums)