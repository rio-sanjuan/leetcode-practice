class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        result = 0
        i = 0
        n = len(s)

        max_num = pow(2, 31) - 1
        min_num = -1 * pow(2, 31)

        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] == "+":
            sign = 1
            i += 1
        elif i < n and s[i] == "-":
            sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            new_num = result * 10 + digit

            if new_num > max_num:
                return max_num if sign > 0 else min_num

            result = new_num
            i += 1

        return sign * result


# if (result * 10 > max_num) or (result * 10 == max_num and digit > max_num % 10):
#                 return max_num if sign > 0 else min_num
