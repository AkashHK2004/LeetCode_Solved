class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st1=str(x)
        st2=""
        for i in range(1,len(st1)+1):
            st2+=st1[len(st1)-i]
        
        if (st1==st2):
            return True
        else:
            return False