from Py.Utils.Definition import ListNode


class Solution(object):
    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 循环
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            node1 = current.next
            node2 = node1.next
            node1.next = node2.next
            node2.next = node1
            current.next = node2
            current = current.next.next
        return dummy.next

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs2(head.next.next)
        second.next = head
        return second


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    p = head
    while p:
        print(p.val)
        p = p.next

    print('\n')
    Sol = Solution()
    p = Sol.swapPairs2(head)
    while p:
        print(p.val)
        p = p.next