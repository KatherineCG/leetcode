class SingleList():
    def __int__(self):
        self._head = None

    def length(self):
        cur = self._head
        len = 0
        while cur:
            len += 1
            cur = cur.next

        return len


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1.length() > 50 or list2.length() > 50:
            return

        if list1._head is None:
            return list2

        if list2._head is None:
            return list1

        resultList = SingleList()

        curList1Node = list1._head
        curList2Node = list2._head

        if curList1Node.val < -100 or curList1Node.val > 100:
            return

        if curList2Node.val < -100 or curList2Node.val > 100:
            return

        if curList1Node.val <= curList2Node.val:
            resultList._head = curList1Node
            curList1Node = curList1Node.next
        else:
            resultList._head = curList2Node
            curList2Node = curList2Node.next

        curResListNode = resultList._head

        while curList1Node and curList2Node:
            if curList1Node.val < -100 or curList1Node.val > 100:
                return

            if curList2Node.val < -100 or curList2Node.val > 100:
                return

            if curList1Node.val <= curList2Node.val:
                curResListNode.next = curList1Node
                curList1Node = curList1Node.next
            else:
                curResListNode.next = curList2Node
                curList2Node = curList2Node.next

            curResListNode = curResListNode.next

        if curList1Node:
            curResListNode.next = curList1Node

        if curList2Node:
            curResListNode.next = curList2Node

        return resultList

if __name__ == '__main__':
    test = Solution()

    list1, list2 = SingleList(), SingleList()
    list1Node1 = ListNode(1)
    list1Node2 = ListNode(2)
    list1Node3 = ListNode(4)
    list1._head = list1Node1
    list1Node1.next = list1Node2
    list1Node2.next = list1Node3

    list2Node1 = ListNode(1)
    list2Node2 = ListNode(3)
    list2Node3 = ListNode(4)
    list2._head = list2Node1
    list2Node1.next = list2Node2
    list2Node2.next = list2Node3

    resultList = test.mergeTwoLists(list1, list2)
    resNode = resultList._head
    while resNode:
        print(resNode.val)
        resNode = resNode.next