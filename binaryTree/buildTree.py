#105
#用前序和中序遍历的数组，来一起构件一个二叉树
class Solution:
    def buildTree(self, preorder, inorder):
        pre_len = len(preorder)
        in_len = len(inorder)
        map_head = dict()
        for i in range(in_len):
            map_head[inorder[i]] = i
        root = self.f(preorder,0,pre_len-1,inorder,0,in_len-1,map_head)
        return root

    def f(self,preorder,l1,r1,inorder,l2,r2,map_head):
        if l1 > r1:
            return None
        headNode = TreeNode(preorder[l1])
        head = map_head[preorder[l1]]
        if l1 == r1:
            return headNode
        #l1 l1+1 ... l1+head-l2 ... r1
        #l2 l2+1 ... head head+1 ... r2
        headNode.left = self.f(preorder,l1+1,l1+head-l2,inorder,l2,head-1,map_head)
        headNode.right = self.f(preorder,l1+head-l2+1,r1,inorder,head+1,r2,map_head)
        return headNode

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    #print(s.serialize(root))
    s.buildTree([3,9,20,15,7],[9,3,15,20,7])
    pass
