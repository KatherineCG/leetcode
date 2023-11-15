class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] < -100 or nums[i] > 100:
                return

            if nums[i] in nums[i+1:]:
                nums.remove(nums[i])
            else:
                i += 1

        return nums

if __name__ == '__main__':
    test = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(test.removeDuplicates(nums))

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, x in enumerate(sorted(set(nums))): nums[i] = x
        return i + 1
'''

'''
class Solution:
    def removeDuplicates(self, nums):
        nums[:]=list(set(nums))
        nums.sort()
        return len(nums)
 
@Mr Chen 感觉不是这个问题吧，最后输出的是列表，set转list会自动排序的；AI给出的原因是： 
nums[:]=list(set(nums)) 和 nums= list(set(nums)) 的区别在于对原始列表 nums 的影响。

nums[:]=list(set(nums))：这行代码使用了切片操作符 [:]，它会将列表 nums 转换为集合，
以去除重复元素，然后再将集合转换回列表，并将结果赋值给 nums 的切片操作 nums[:]。
这样做会修改原始列表 nums，使其变为不包含重复元素的有序列表。原始列表 nums 的内容会被改变。

nums= list(set(nums))：这行代码将列表 nums 转换为集合，以去除重复元素，然后将集合转换回列表
并将结果赋值给变量 nums。这样做不会修改原始列表 nums，而是创建了一个新的列表 nums，
其中包含了去重后的有序元素。原始列表 nums 的内容不会被改变。
'''