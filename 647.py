class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i,j = 0,0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    result += 1
        return result
