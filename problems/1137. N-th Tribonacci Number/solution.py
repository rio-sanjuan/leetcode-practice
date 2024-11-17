import numpy as np


class Solution(object):
    def trib_memo(self, n):
        mem = {}

        def sub_fun(n):
            if n <= 0:
                return 0
            elif n <= 2:
                return 1

            if n not in mem:
                mem[n] = sub_fun(n - 1) + sub_fun(n - 2) + sub_fun(n - 3)

            return mem[n]

        return sub_fun(n)

    def trib_tab(self, n):
        if n <= 0:
            return 0
        elif n <= 2:
            return 1

        ans = [0] * (n + 1)
        ans[0] = 0
        ans[1] = 1
        ans[2] = 1

        for i in range(3, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

        return ans[-1]

    def mat_mult(self, m1, m2):
        return np.matmul(m1, m2)

    def mat_pow(self, m, n):
        result = np.identity(len(m))
        base = m

        while n > 0:
            if n % 2 == 1:
                result = self.mat_mult(result, base)

            base = self.mat_mult(base, base)
            n //= 2

        return result

    def trib_mult(self, n):
        if n <= 0:
            return 0
        elif n <= 2:
            return 1

        tribonacci_mat = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        return int(self.mat_pow(tribonacci_mat, n - 1)[0][0])

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.trib_mult(n)
