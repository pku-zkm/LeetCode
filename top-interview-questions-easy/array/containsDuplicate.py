class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return False
        nums.sort()
        a=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=a:
                a=nums[i]
            else:
                return True
        return False

s=Solution()
print(s.containsDuplicate([1,2,3,1]))