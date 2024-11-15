class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[nums[i]] = i
        return []
