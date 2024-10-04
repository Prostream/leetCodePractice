#297-二叉树的序列化与反序列化,可以用前序遍历的方式，也可以用层序遍历的方式（进序列同时序列化，如果是空节点，只需要序列化不进队列）
#
from itertools import count

from binaryTree.widthofBinaryTree import TreeNode


class Codec(object):
    def serialize(self, root):
        string = ""
        string = self.f(root, string)
        return string

    def deserialize(self, data):
        string_array = data.split(',')
        string_array.pop()
        root = self.g(string_array)
        return root

    #前序遍历的序列号，顺带一提中序遍历不行
    def f(self, root, string):
        if not root:
            return string + "#,"
        else:
            string = string + str(root.val) + ","
            string = self.f(root.left, string)
            string = self.f(root.right, string)
            return string

    count = 0
    def g(self, string):
        if not string:
            return None
        #notation  1 # 3 # #
        if self.count >= len(string)-1 or string[self.count] == "#":
            self.count = self.count + 1
            return None
        else:
            node = TreeNode(string[self.count])
            self.count = self.count + 1
            node.left = self.g(string)
            node.right = self.g(string)
            return node

if __name__ == '__main__':
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    s = Codec()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    #print(s.serialize(root))

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))