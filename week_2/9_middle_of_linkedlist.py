# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        idx = 0
        curr = head
        while idx != length // 2:
            curr = curr.next
            idx += 1
        return curr

    def middle_node_using_fast_slow_ptrs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        if not head.next.next:
            return head.next
        slow = head.next
        fast = head.next.next
        while slow and fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        return slow


def test_middle_of_linkedlist():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().middle_node(head)
    assert result.val == 3
    result = Solution().middle_node_using_fast_slow_ptrs(head)
    assert result.val == 3


if __name__ == "__main__":
    test_middle_of_linkedlist()
