class Solution(object):
    def maxAreaBruteForce(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))

        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, cur_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
