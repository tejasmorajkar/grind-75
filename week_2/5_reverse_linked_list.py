from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr.next = prev
            prev = curr
            curr = curr.next
        return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = Solution().reverse_list(head)
while result:
    print(result.val, end=" ")
    result = result.next
