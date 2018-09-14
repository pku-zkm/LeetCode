class Solution:
    # def intersect(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     d1=dict.fromkeys(nums1,0)
    #     d2=dict.fromkeys(nums1,0)
    #     for a in nums1:
    #         d1[a]+=1
    #     for a in nums2:
    #         if d2.get(a) is not None:
    #             d2[a]+=1
    #     arr=[]
    #     for k in d1.keys():
    #         n=d1[k] if d1[k] < d2[k] else d2[k]
    #         for i in range(n):
    #             arr.append(k)
    #     return arr

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        arr=[]
        i,j=0,0
        n1,n2=len(nums1),len(nums2)
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                arr.append(nums1[i])
                i,j=i+1,j+1
        return arr
