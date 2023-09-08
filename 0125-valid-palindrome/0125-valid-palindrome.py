class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str=''
        for i in s.lower():
            if i.isalnum():
                str+=i
        if (str==str[::-1]):
            return True
        else:
            return False
 