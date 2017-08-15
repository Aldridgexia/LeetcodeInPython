class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        else:
            res = [1 for _ in range(len(nums))]
            for i in range(1,len(nums)):
                for j in range(0,i):
                    if nums[j] < nums[i]:
                        res[i] = max(res[i],res[j] + 1)
            return max(res)      
