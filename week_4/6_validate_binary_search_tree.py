from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], left: float, right: float) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, -math.inf, math.inf)


def test_valid_bst():
    root = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7)))
    actual = Solution().is_valid_bst(root)
    assert not actual, f"Test for valid bst failed. Expected False, but got {actual}"
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    actual = Solution().is_valid_bst(root)
    assert actual, f"Test for valid bst failed. Expected True, but got {actual}"


if __name__ == "__main__":
    test_valid_bst()
