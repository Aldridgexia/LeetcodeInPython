class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            result = [x for row in nums for x in row]
            result = [[result[c * i + j] for j in range(c)] for i in range(r)]
            return result
