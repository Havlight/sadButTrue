class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        is_swapped = False
        if root:
            self.recoverTree(root.left)
            r_node = self._dfs_right(root, root.right)
            l_node = self._dfs_left(root, root.left)
            if r_node and l_node:
                r_node.val, l_node.val = l_node.val, r_node.val
                is_swapped = True
            elif r_node:
                r_node.val, root.val = root.val, r_node.val
                is_swapped = True
            elif l_node:
                l_node.val, root.val = root.val, l_node.val
                is_swapped = True
            if is_swapped:
                return
            self.recoverTree(root.right)

    def _dfs_right(self, head: TreeNode, node: TreeNode):
        if not node:
            return None
        if node.val > head.val:
            tmp = None
            if node.left:
                tmp = self._dfs_right(head, node.left)
            if node.right:
                tmp = self._dfs_right(head, node.right)
            if tmp:
                return tmp
        else:
            return node

    def _dfs_left(self, head: TreeNode, node: TreeNode):
        if not node:
            return None
        if node.val < head.val:
            tmp = None
            if node.left:
                tmp = self._dfs_right(head, node.left)
            if node.right:
                if not tmp:
                    tmp = self._dfs_right(head, node.right)
            if tmp:
                return tmp
        else:
            return node
