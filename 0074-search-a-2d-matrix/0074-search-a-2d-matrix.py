class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col=len(matrix[0])
        s=0
        e=row*col-1
        while(s<=e):
            mid=s+(e-s)/2
            ele=matrix[mid/col][mid%col]
            if(ele==target):
                return True
            elif(ele<target):
                s=mid+1
            else:
                e=mid-1
        return False
        