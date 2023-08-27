class Solution(object):
    def twoSum(self, nums , target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst=[]
        for i in range(len(nums)):
            for j in range(i):
                if target==nums[i]+nums[j]:
                    lst.append(j)
                    lst.append(i)
                    break
        return lst                
