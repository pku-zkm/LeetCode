class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        if target%2==0:
            a=target//2
            try:
                i=nums.index(a)
                j=nums.index(a,i+1)
                return [i,j]
            except ValueError as e:
                pass

        d={}
        for i in range(n):
            d[nums[i]]=i
        for k in d.keys():
            if k==target-k:
                continue
            if d.get(target-k) is not None:
                i=d[k]
                j=d[target-k]
                if i>j:
                    i,j=j,i
                return [i,j]

s=Solution()
print(s.twoSum([3,2,4],6))