class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_string = str(x)
        length = len(x_string)

        # Environment setting
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)

        result = 0
        negative = 0
        multi = 1
        for i in range(length):
            if x_string[i] == '-':
                negative = 1
            else:
                result += int(x_string[i]) * multi
                multi *= 10
        if result > int_max or result < int_min:
            return 0
        elif negative:
            return -result
        else:
            return result