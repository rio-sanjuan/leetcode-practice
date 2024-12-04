class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        for c in s:
            if c not in mem:
                mem[c] = 1
            else:
                mem[c] += 1

        for i, c in enumerate(s):
            if mem[c] == 1:
                return i
        return -1
