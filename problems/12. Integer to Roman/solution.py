class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        ones = int(num % 10)
        if ones == 0:
            pass
        elif ones < 4:
            result += "I" * ones
        elif ones == 4:
            result += "VI"
        elif ones < 9:
            result += "I" * (ones - 5) + "V"
        elif ones == 9:
            result += "XI"

        tens = int(num // 10 % 10)
        if tens == 0:
            pass
        elif tens < 4:
            result += "X" * tens
        elif tens == 4:
            result += "LX"
        elif tens < 9:
            result += "X" * (tens - 5) + "L"
        elif tens == 9:
            result += "CX"

        hund = int(num // 100 % 10)
        if hund == 0:
            pass
        elif hund < 4:
            result += "C" * hund
        elif hund == 4:
            result += "DC"
        elif hund < 9:
            result += "C" * (hund - 5) + "D"
        elif hund == 9:
            result += "MC"

        thou = int(num // 1000 % 10)
        if thou > 0:
            result += "M" * int(thou)

        return result[::-1]
