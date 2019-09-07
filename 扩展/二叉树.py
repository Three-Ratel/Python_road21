"""
1. 列表判断法
2. 3种深度遍历
"""


# 封装一个节点对象
class Node(object):

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree(object):
    # 实例化出一个空的二叉树对象
    def __init__(self):
        # 如果root=None则，二叉树为空
        self.root = None

    # 向二叉树中插入节点
    def addNode(self, item):
        node = Node(item)
        if not self.root:
            # 树为空
            self.root = node
            return

        # 树非空
        cur = self.root
        queue = [cur]
        # # 列表判断法
        # while True:
        #     n = queue.pop(0)
        #     if n.left:
        #         queue.append(n.left)
        #     else:
        #         n.left = node
        #         return
        #     if n.right:
        #         queue.append(n.right)
        #     else:
        #         n.right = node
        #         return

        # # 自己实现，list可能会很长，也就是说牺牲了空间，换取时间
        for i in queue:
            if i.left:
                queue.append(i.left)
            else:
                i.left = node
                print(len(queue))
                return
            if i.right:
                queue.append(i.left)
            else:
                i.right = node
                print(len(queue))
                return

    # 遍历
    def travel(self):
        if not self.root:
            print('树为空')
            return

        cur = self.root
        queue = [cur]
        while queue:
            n = queue.pop(0)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            print(n.item, end='  ')

    # 前序遍历(从小到大)
    def forward(self, root):
        # root是不同子树的根
        if not root:
            return
        print(root.item, end='  ')
        self.forward(root.left)
        self.forward(root.right)

    # 中序遍历
    def middle(self, root):
        # root是不同子树的根
        if not root:
            return
        self.middle(root.left)
        print(root.item, end='  ')
        self.middle(root.right)

    # 后序遍历
    def back(self, root):
        # root是不同子树的根
        if not root:
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item, end='  ')


tree = Tree()
tree.addNode(1)
tree.addNode(2)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(6)
tree.addNode(7)
# print('广度遍历:', end=' ')
# tree.travel()
# print('前序遍历:', end=' ')
# tree.forward(tree.root)
# print('中序遍历:', end=' ')
# tree.middle(tree.root)
# print('后序遍历:', end=' ')
# tree.back(tree.root)
