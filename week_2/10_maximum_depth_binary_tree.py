# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depth = 0

    def _dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self._dfs(node.left) + 1
        right = self._dfs(node.right) + 1
        curr_depth = max(left, right)
        self.depth = max(self.depth, curr_depth)
        return curr_depth

    def max_depth(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)
        return self.depth


def test_maximum_depth_binary_tree():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = Solution().max_depth(root)
    assert result == 3
    root = TreeNode(1, None, TreeNode(2))
    result = Solution().max_depth(root)
    assert result == 2


if __name__ == "__main__":
    test_maximum_depth_binary_tree()