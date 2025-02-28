import math

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_digits = len(digits)
        multi = pow(10, len_digits-1)
        num = 0
        for i in range(len_digits):
            num += digits[i] * multi
            multi /= 10
        num += 1
        len_num = int(math.log10(num)) + 1
        div = pow(10, len_num-1)
        result = []
        for i in range(len_num):
            result.append(num/div)
            num %= div
            div /= 10
        return result