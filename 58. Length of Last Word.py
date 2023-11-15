class Solution:
    def lengthOfLastWord(self, s):
        sList = s.strip().split(' ')
        #sList = list(filter(lambda x:x!='', sList))
        return len(sList[-1])

if __name__ == '__main__':
    test = Solution()
    s = "   fly me   to   the moon  "
    print(test.lengthOfLastWord(s))