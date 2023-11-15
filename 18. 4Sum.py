class Solution:
    def fourSum(self, nums, target):
        length = len(nums)
        if not nums or length > 200:
            return

        i, j= 0, length -1
        nums = sorted(nums)
        resList = []
        while i < j:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            if j < length - 1 and nums[j] == nums[j + 1]:
                j -= 1
                continue

            if nums[i] > target:
                break

            if nums[i] + nums[j] > target:
                j -= 1
                continue

            p, q = i + 1, j - 1
            while p < q:
                resTarget = nums[i] + nums[j]
                tempList = [nums[i], nums[j]]
                if p > i + 1 and nums[p] == nums[p - 1]:
                    p += 1
                    continue

                if q < j - 1 and nums[q] == nums[q + 1]:
                    q -= 1
                    continue

                if nums[p] + resTarget > target:
                    break

                if nums[p] + nums[q] + resTarget > target:
                    q -= 1
                    continue

                if nums[p] + nums[q] + resTarget == target:
                    tempList.append(nums[p])
                    tempList.append(nums[q])
                    if tempList not in resList:
                        resList.append(tempList)

                    p += 1

            i += 1
            j = length - 1

        return resList



if __name__ == '__main__':
    test = Solution()
    nums = [2, 2, 2, 2, 2]
    target = 8
    print(test.fourSum(nums, target))