class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m < 0 or m > 200 or n < 0 or n > 200:
            return

        if m+n < 0 or  m+n > 200:
            return

        if len(nums1) is not m+n:
            return

        if len(nums2) is not n:
            return

        nums1[m:] = nums2
        nums1.sort()

        return nums1

if __name__ == '__main__':
    test = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(test.merge(nums1, m, nums2, n))