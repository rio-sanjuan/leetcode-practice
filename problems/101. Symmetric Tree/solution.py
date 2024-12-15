# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, ltree, rtree):
        if ltree is None and rtree is None:
            return True
        elif ltree is None or rtree is None:
            return False

        return (
            ltree.value == rtree.value
            and self.isMirror(ltree.right, rtree.left)
            and self.isMirror(ltree.left, rtree.right)
        )
