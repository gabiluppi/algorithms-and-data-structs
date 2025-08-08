# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        result_p, null_pos_p = self.inorder(p)
        result_q, null_pos_q = self.inorder(q)
        return result_p == result_q and null_pos_p == null_pos_q

    
    def inorder(self, root):
        result = []
        null_pos = []
        pos = 0
        self._inorder_recursive(root, result, pos, null_pos)
        return result, null_pos

    def _inorder_recursive(self, node, result, pos, null_pos):
        if node is None:
            null_pos.append(pos)

        pos += 1    
        if node:
            self._inorder_recursive(node.left, result, pos, null_pos)
            result.append(node.val)
            self._inorder_recursive(node.right, result, pos, null_pos)