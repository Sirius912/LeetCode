import numpy as np

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        roman = np.zeros(length, dtype=int)
        result = 0
        for i in range(length):
            if s[i] == 'I':
                roman[i] = 1
            elif s[i] == 'V':
                roman[i] = 5
            elif s[i] == 'X':
                roman[i] = 10
            elif s[i] == 'L':
                roman[i] = 50
            elif s[i] == 'C':
                roman[i] = 100
            elif s[i] == 'D':
                roman[i] = 500
            elif s[i] == 'M':
                roman[i] = 1000

        for i in range(length):
            if i == length - 1 or roman[i] >= roman[i+1]:
                result += roman[i]
            else:
                result -= roman[i]
                
        return result