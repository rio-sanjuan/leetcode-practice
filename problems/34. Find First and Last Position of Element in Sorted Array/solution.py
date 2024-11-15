class Solution(object):
    def binarySearch(self, nums, target, find_first=True):
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2
            split = nums[mid]

            if split == target:
                index = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif split < target:
                left = mid + 1
            else:
                right = mid - 1

        return index

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lidx = self.binarySearch(nums, target, find_first=True)
        ridx = self.binarySearch(nums, target, find_first=False)
        return [lidx, ridx]
