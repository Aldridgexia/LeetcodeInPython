class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        result = []
        for n in nums2:
            try:
                if nums1.index(n) >= 0:
                    result.append(nums1.pop(nums1.index(n)))
            except ValueError:
                pass
        return result
