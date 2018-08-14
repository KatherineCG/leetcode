class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        maxint = 2 ** 31 - 1
        minint = -1 * 2 ** 31
        if x < 0:
            result = -1 * int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])
        if result > maxint or result < minint:
            result = 0
        return result
test = Solution()
x = input()
print test.reverse(x)