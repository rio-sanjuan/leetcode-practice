class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        return nums[n - k]

    def findKthLargestWithoutSorting(self, nums, k):
        import heapq

        # this can be done using a min-heap with at most k elements
        # iterate through elements in num
        # if size > k, pop min-heap
        # finally return top of the heap (kth min value)
        # This has O(n log k) complexity
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
sol.findKthLargest(nums, k)
sol.findKthLargestWithoutSorting(nums, k)
