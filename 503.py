class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res = [], [-1 for i in range(len(nums))]
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        if stack:
            for i in range(stack[0] + 1):
                while nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
        return res
