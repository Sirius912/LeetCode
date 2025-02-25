class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_length = len(s)
        result = 0
        
        # start from the end
        for i in range(s_length - 1, -1, -1):
            if s[i] == ' ':
                if result == 0:
                    continue
                else:
                    break
            else:
                result += 1

        return result