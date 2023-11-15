class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[(length - k):] + nums[:(length - k)]
        return nums

        # 方法2
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]

if __name__ == '__main__':
    test = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(test.rotate(nums, k))