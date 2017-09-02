class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                if sorted(nums) == nums:
                    return True
                nums[i] = temp
                nums[i + 1] = nums[i]
                if sorted(nums) == nums:
                    return True
                return False
        return True
