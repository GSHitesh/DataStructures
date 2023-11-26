class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count = count + 1
            temp = temp.next

        # If there's only one node or we need to remove the first node, return head.next
        if count == 1 or n == count:
            return head.next

        new_n = count - n + 1
        temp = head

        # Move temp to the node before the one to be removed
        for _ in range(0, new_n - 2):
            temp = temp.next

        # If temp.next is not None, update temp's next pointer
        if temp.next:
            temp.next = temp.next.next

        return head
