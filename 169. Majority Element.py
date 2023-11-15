class Solution:
    def majorityElement(self, nums):
        majorityNum = len(nums) / 2
        for num in set(nums):
            if nums.count(num) > majorityNum:
                return num

if __name__ == '__main__':
    test = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(test.majorityElement(nums))