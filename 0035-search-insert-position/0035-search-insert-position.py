class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(nums)
        if(nums[e-1]<target):
            return e
        while(s<=e):
            mid=s+(e-s)/2
            if(nums[mid]==target):
                return mid;
            elif(nums[mid]<target):
                s=mid+1
            else:
                e=mid-1
        return s
        