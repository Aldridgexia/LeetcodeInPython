class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1 for _ in findNums]
        for i,n in enumerate(findNums):
            idx = nums.index(n)
            for j in range(idx, len(nums)):
                if nums[j] > n:
                    result[i] = nums[j]
                    break
        return result
