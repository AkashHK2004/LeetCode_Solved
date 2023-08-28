class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        st1=str(x)
        st2=""

        if st1[0]=='-':
            
            for i in range(1,len(st1)):
                st2+=st1[len(st1)-i]
            n=-(int(st2))
        else:
            for i in range(1,len(st1)+1):
                st2+=st1[len(st1)-i]
            n=int(st2)
        if n>(-2**31) and n<((2**31)-1):
            return n
        else:
            return 0
        
        
