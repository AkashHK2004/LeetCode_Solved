class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans=""
        carry= 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry!= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            ans = str(sum % 2) + ans
            carry=sum // 2
        return ans
            

        