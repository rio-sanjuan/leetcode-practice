class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        split = nums[mid]
        while left <= right:
            if target == split:
                return mid
            elif target < split:
                right = mid - 1
            else:
                left = mid + 1

            mid = (left + right) // 2
            split = nums[mid]
        return left
