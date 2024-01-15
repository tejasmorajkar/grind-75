# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr

    def lowest_common_ancestor_using_recursion(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowest_common_ancestor_using_recursion(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowest_common_ancestor_using_recursion(root.left, p, q)
        else:
            return root


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

result = Solution().lowest_common_ancestor_using_recursion(root, TreeNode(2), TreeNode(8))
print(result.val)

result = Solution().lowest_common_ancestor_using_recursion(root, TreeNode(2), TreeNode(4))
print(result.val)
