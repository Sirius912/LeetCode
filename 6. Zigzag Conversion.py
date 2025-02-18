class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        w, h = length/2, numRows
        Matrix = [[' ' for x in range(w)] for y in range(h)]

        x, y = 0, 0
        for i in range(length):
            print(s[i])
            print('=========x, y, i', x, y, i)
            if y < numRows:
                if x == 0:
                    print('===17===')
                    print('x, y, i', x, y, i)
                    Matrix[y][x] = s[i]
                    y += 1

                elif x % (numRows - 1) == 0:
                    print('===22===')
                    # print('x, y', x, y)
                    y += 1
                    print('x, y', x, y)

                    Matrix[y][x] = s[i]

                    y += 1
                else:
                    print('===27===')
                    y -= 1
                    x += 1
                    print('x, y', x, y)
                    Matrix[y][x] = s[i]
            else:
                print('===32===')
                y -= 2
                x += 1
                print('x, y', x, y)
                Matrix[y][x] = s[i]
            for row in Matrix:
                print(row)


        # for row in Matrix:
        #     print(row)