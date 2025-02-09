class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constraints 1
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)

        if dividend > 0 and divisor > 0:
            result = abs(dividend) / abs(divisor)
        elif dividend < 0 and divisor < 0:
            result = abs(dividend) / abs(divisor)
        else:
            result = -(abs(dividend) / abs(divisor))

        if result >= int_max:
            result = int_max
        elif result <= int_min:
            result = int_min

        return result