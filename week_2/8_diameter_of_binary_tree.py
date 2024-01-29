# https://leetcode.com/problems/diameter-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def _dfs(self, node: Optional[TreeNode], curr_height: int) -> int:
        if not node:
            return -1
        left_height = self._dfs(node.left, curr_height + 1) + 1
        right_height = self._dfs(node.right, curr_height + 1) + 1
        self.result = max(self.result, left_height + right_height)
        return max(left_height, right_height)

    def diameter_of_binarytree(self, root: Optional[TreeNode]) -> int:
        self._dfs(root, 0)
        return self.result


def test_diameter_binary_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    result = Solution().diameter_of_binarytree(root)
    print(result)


if __name__ == "__main__":
    test_diameter_binary_tree()
