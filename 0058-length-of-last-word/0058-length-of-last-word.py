class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=s.split()
        st=lst[len(lst)-1]
        return len(st)