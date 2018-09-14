class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        if digits[-1]==9:
            for i in range(n-1,-1,-1):
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    break
            if digits[0]==0:
                digits.insert(0,1)
        else:
            digits[-1]+=1
        return digits