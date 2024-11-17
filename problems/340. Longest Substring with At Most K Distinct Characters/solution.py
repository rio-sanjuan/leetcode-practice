class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0
        char_freq = {}
        l_idx = max_len = 0
        for r_idx, char in enumerate(s):
            char_freq[char] = char_freq.get(char, 0) + 1

            while len(char_freq) > k:
                left_char = s[l_idx]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                l_idx += 1

            cur_len = r_idx - l_idx + 1
            max_len = max(max_len, cur_len)

        return max_len
