class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        n = len(s)

        while i < n:
            can_lookahead = i + 1 < n

            if s[i] == "I":
                if can_lookahead and s[i + 1] == "V":
                    result += 4
                    i += 1
                elif can_lookahead and s[i + 1] == "X":
                    result += 9
                    i += 1
                else:
                    result += 1
            elif s[i] == "V":
                result += 5
            elif s[i] == "X":
                if can_lookahead and s[i + 1] == "L":
                    result += 40
                    i += 1
                elif can_lookahead and s[i + 1] == "C":
                    result += 90
                    i += 1
                else:
                    result += 10
            elif s[i] == "L":
                result += 50
            elif s[i] == "C":
                if can_lookahead and s[i + 1] == "D":
                    result += 400
                    i += 1
                elif can_lookahead and s[i + 1] == "M":
                    result += 900
                    i += 1
                else:
                    result += 100
            elif s[i] == "D":
                result += 500
            elif s[i] == "M":
                result += 1000

            i += 1

        return result
