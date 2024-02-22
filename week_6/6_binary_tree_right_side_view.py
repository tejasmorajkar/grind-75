# https://leetcode.com/problems/binary-tree-right-side-view/
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def level_order_traversal(node: Optional[TreeNode]) -> List[List[int]]:
            if node is None:
                return []
            q = collections.deque()
            q.append(node)
            traversal = []
            while q:
                q_size = len(q)
                new_level = []
                for _ in range(q_size):
                    curr = q.popleft()
                    new_level.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                traversal.append(new_level)
            return traversal

        levels = level_order_traversal(root)
        result = []
        for level in levels:
            result.append(level[-1])
        return result


def test_binary_tree_right_side_view():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    result = Solution().rightSideView(root)
    print(result)
    root = TreeNode(1, None, TreeNode(3))
    result = Solution().rightSideView(root)
    print(result)
    root = None
    result = Solution().rightSideView(root)
    print(result)


if __name__ == "__main__":
    test_binary_tree_right_side_view()
