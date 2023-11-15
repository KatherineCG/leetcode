class Solution:
    def removeElement(self, numsList, val):
        if not numsList or len(numsList) > 100:
            print("Length of list not fix the limitation")
            return

        if val < 0 or val > 50:
            print("Val %s not fix the limitation" % val)
            return

        i = 0
        while i != len(numsList):
            if numsList[i] < 0 or numsList[i] > 50:
                print("Element %s in list not fix the limitation" % numsList[i])
                return

            if numsList[i] == val:
                numsList.remove(numsList[i])
            else:
                i += 1

        return numsList


if __name__ == '__main__':
    test = Solution()
    numsList = [0,1,2,2,3,0,4,2]
    val = 2
    print(test.removeElement(numsList, val))
