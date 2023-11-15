class Solution:
    def findMaximumXOR(self, nums):
        if not nums:
            return

        if any(num < 0 for num in nums):
            return

        result = 0
        i, j = 0, 0
        length = len(nums)
        while i < length:
            j = i + 1
            while j < length:
                result = max(nums[i] ^ nums[j], result)
                j += 1

            i += 1

        return result

if __name__ == '__main__':
    test = Solution()
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    print(test.findMaximumXOR(nums))