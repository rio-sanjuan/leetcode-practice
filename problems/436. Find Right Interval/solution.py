class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        answer = [-1] * n
        intervals = sorted(
            [(start, end, idx) for idx, (start, end) in enumerate(intervals)]
        )
        intervals.append((float("inf"), float("inf"), -1))

        for i in range(n):
            _, e1, i1 = intervals[i]
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                s2, _, _ = intervals[mid]
                if s2 >= e1:
                    right = mid - 1
                else:
                    left = mid + 1
            answer[i1] = intervals[left][2]

        return answer
