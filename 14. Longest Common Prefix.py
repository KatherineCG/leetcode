class Solution:
    def longestCommonPrefix(self, strs):
        commonPrefix = min(strs, key=lambda str: len(str))
        while commonPrefix:
            if all(str.startswith(commonPrefix) for str in strs):
                break
            else:
                commonPrefix = commonPrefix[:-1]
        return commonPrefix

if __name__ == '__main__':
    test = Solution()
    strs = ["dog","racecar","car"]
    print(test.longestCommonPrefix(strs))