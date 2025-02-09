class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            # Convert the integer to a string
            x = str(x)
            length = len(x)
            for i in range(length):
                if x[i] != x[length-i-1]:
                    return False
                else:
                    continue
            return True