class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        for a in nums:
            r=r^a
        return r

s=Solution()
print(s.singleNumber( [4,1,2,1,2]))
