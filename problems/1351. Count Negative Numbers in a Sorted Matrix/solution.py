class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neg_count = 0

        # snake through the matrix, starting bottom-left
        i, j = len(grid) - 1, 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                neg_count += len(grid[i]) - j
                i -= 1
            else:
                j += 1

        return neg_count
