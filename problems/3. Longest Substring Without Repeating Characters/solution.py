class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        l_idx = max_len = 0
        for r_idx, c in enumerate(s):
            # 1. check if seen
            if c in mem and mem[c] >= l_idx:
                l_idx = mem[c] + 1

            # 2. update mem
            mem[c] = r_idx

            # 3. update max_len
            cur_len = r_idx - l_idx + 1
            max_len = max(max_len, cur_len)

        return max_len
