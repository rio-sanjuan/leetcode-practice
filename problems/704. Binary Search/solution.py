class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l0 = 0
        l1 = len(nums) - 1
        lmid = (l0 + l1) // 2
        split = nums[lmid]
        while l0 <= l1:
            if split == target:
                return lmid
            elif split < target:
                l0 = lmid + 1
            else:
                l1 = lmid - 1
            lmid = (l0 + l1) // 2
            split = nums[lmid]
        return -1
