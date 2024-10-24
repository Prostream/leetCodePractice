#same tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def compare(treeA,treeB):
            if treeA is None and treeB is None:
                return True
            if (treeA is None and treeB is not None) or (treeA is not None and treeB is None):
                return False
            if treeA.val != treeB.val:
                return False
            if compare(treeA.left,treeB.left) and compare(treeA.right,treeB.right):
                return True

        return compare(p,q)