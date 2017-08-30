class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        if not nums:
            return res
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                if temp > res:
                    res = temp
                temp = 0
            if temp > res:
                    res = temp
        return res
