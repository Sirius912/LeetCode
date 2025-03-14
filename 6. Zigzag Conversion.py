class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        w, h = length, numRows
        Matrix = [[' ' for x in range(w)] for y in range(h)]

        print('numRows =', h)
        x, y = 0, 0
        for i in range(length):
            if x == 0 and y == 0:
                Matrix[y][x] = s[i]
                y += 1
            elif y < numRows:
                Matrix[y][x] = s[i]
                y += 1
            elif y == numRows:
                y -= 2
                x += 1
                Matrix[y][x] = s[i]
                y -= 1
                x += 1
            elif (y % numRows) == 0:
                Matrix[y][x] = s[i]
                y += 1
            for row in Matrix:
                print(row)
            print('')

        result = ''
        for row in Matrix:
            for char in row:
                if char != ' ':
                    result += char
        return result