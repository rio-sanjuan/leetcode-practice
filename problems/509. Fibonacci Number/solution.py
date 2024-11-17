class Solution(object):
    def fib_tabulation(self, n):
        if n <= 1:
            return 1

        ans = [0] * n
        ans[0] = ans[1] = 1
        for i in range(2, n):
            ans[i] = ans[i - 1] + ans[i - 2]

        return ans[-1]

    def fib_memoization(self, n):
        if n <= 1:
            return 1

        mem = {}

        def sub_fib(n, mem={}):
            if n not in mem:
                mem[n] = sub_fib(n - 1, mem) + sub_fib(n - 2, mem)

            return mem[n]

        return sub_fib(n, mem)

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fib_tabulation(self, n)
