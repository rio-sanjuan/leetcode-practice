class Solution(object):
    def twoSumII(self, nums, i, res):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0:
                break
            if i == 0 or sorted_nums[i - 1] != sorted_nums[i]:
                self.twoSumII(sorted_nums, i, result)
        return result
