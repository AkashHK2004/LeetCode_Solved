class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]+=nums[i+1]
                nums[i+1]=0
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                j+=1
        for i in range(j,len(nums)):
            nums[i]=0
        return nums

        