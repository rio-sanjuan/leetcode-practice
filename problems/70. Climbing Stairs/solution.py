import numpy as np
from functools import lru_cache


class Solution(object):
    def multiply_matrices(self, m1, m2):
        return [
            [
                m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0],
                m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1],
            ],
            [
                m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0],
                m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1],
            ],
        ]

    def matrix_power(self, matrix, n):
        result = [[1, 0], [0, 1]]
        base = matrix

        while n > 0:
            if n % 2 == 1:
                result = self.multiply_matrices(result, base)
            base = self.multiply_matrices(base, base)
            n //= 2
        return result

    def recursiveClimbStairs(self, n):
        # O(2^n)
        if n <= 1:
            return 1
        return self.recursiveClimbStairs(n - 1) + self.recursiveClimbStairs(n - 2)

    def tabulationClimbStairs(self, n):
        tab = [0] * (n + 1)
        tab[0] = 1
        tab[1] = 1
        for i in range(2, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]
        return tab[-1]

    def memoClimbStairs(self, n):
        memo = {}

        def sol(n):
            if n <= 1:
                return 1
            if n not in memo:
                memo[n] = sol(n - 1) + sol(n - 2)
            return memo[n]

        return sol(n)

    @lru_cache(None)
    def decoMemoClimbStairs(self, n):
        if n <= 1:
            return 1
        return self.decoMemoClimbStairs(n - 1) + self.decoMemoClimbStairs(n - 2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(log n)
        if n <= 1:
            return 1

        fib_matrix = [[1, 1], [1, 0]]
        result = self.matrix_power(fib_matrix, n - 1)
        return result[0][0]
