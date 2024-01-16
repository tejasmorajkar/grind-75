# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.visited = set()
        self.is_cyclic = False

    def _dfs(self, node: Optional[ListNode]):
        if not node:
            return
        if node in self.visited:
            self.is_cyclic = True
            return
        self.visited.add(node)
        self._dfs(node.next)
        

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        self._dfs(head)
        return self.is_cyclic


class Solution2:
    def __init__(self):
        self.is_cyclic = False

    def _dfs(self, node: Optional[ListNode]):
        if not node or not node.next:
            return
        slow = node.next
        fast = node.next.next
        while slow and fast:
            if slow == fast:
                self.is_cyclic = True
                break
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        self._dfs(head)
        return self.is_cyclic


sol1 = Solution()
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
print(sol1.has_cycle(head1))

sol2 = Solution2()
print(sol2.has_cycle(head1))
