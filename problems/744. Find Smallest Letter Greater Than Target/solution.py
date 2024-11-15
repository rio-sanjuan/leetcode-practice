class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        left = 0
        right = len(letters) - 1
        mid = (left + right) // 2
        switch = letters[mid]
        while left <= right:
            if switch > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
            switch = letters[mid]
        return letters[left]
