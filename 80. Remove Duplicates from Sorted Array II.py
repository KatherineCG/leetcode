class Solution:
    def removeDuplicates(self, nums):
        nums1 = list(set(nums))
        nums2 = [num for num in set(nums) if nums.count(num) > 1]
        nums2[:] = list(set(nums2))
        nums[:] = nums1 + nums2
        nums.sort()
        return nums

if __name__ == '__main__':
    test = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(test.removeDuplicates(nums))