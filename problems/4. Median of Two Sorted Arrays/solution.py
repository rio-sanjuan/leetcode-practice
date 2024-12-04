class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if nums % 2 == 1:
            return float(nums[n // 2])
        else:
            return float((nums[n // 2] + nums[n // 2 + 1]) / 2)
