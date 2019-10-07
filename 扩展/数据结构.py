# """单链表：link"""
#
#
# class Node(object):
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# class Link(object):
#
#     def __init__(self):
#         # _head 永远指向link中的头节点
#         self._head = None
#         self._rear = None
#
#     # 头部插入节点
#     def add(self, item):
#         node = Node(item)
#         if not self._rear: self._rear = node
#         node.next = self._head
#         self._head = node
#
#     # 追加元素
#     def append(self, item):
#         node = Node(item)
#         self._rear.next = node
#         self._rear = node
#
#     # # 追加元素
#     # def append(self, item):
#     #     node = Node(item)
#     #     cur = self._head
#     #
#     #     if self._head == None:
#     #         self._head = node
#     #         return
#     #
#     #     while cur:
#     #         pre = cur
#     #         cur = cur.next
#     #     pre.next = node
#
#     def travel(self):
#         cur = self._head
#         if not self._head:
#             print('None')
#
#         while cur:
#             print(cur.item)
#             cur = cur.next
#
#     def isEmpty(self):
#         return self._head == None
#
#     def length(self):
#         cur = self._head
#         count = 0
#         if not self._head:
#             return count
#
#         while cur:
#             count += 1
#             cur = cur.next
#         return count
#
#     def serarch(self, item):
#         cur = self._head
#         find = False
#         while cur:
#             if cur.item == item:
#                 find = True
#                 break
#             cur = cur.next
#         return find
#
#     def insert(self, pos, item):
#         node = Node(item)
#         cur = self._head
#         for i in range(pos - 1):
#             cur = cur.next
#
#         node.next = cur.next
#         cur.next = node
#
#     # 删除item
#     def remove(self, item):
#         cur = self._head
#
#         if not self._head:
#             print('链表为空，没有可删除节点')
#             return
#
#         if self._head.item == item:
#             self._head = self._head.next
#             return
#
#         while cur:
#             pre = cur
#             cur = cur.next
#             if item == cur.item:
#                 pre.next = cur.next
#                 return
#
#
# link = Link()
# # link.add(3)
# # link.add(4)
# # link.add(5)
# # link.append(6)
# # link.insert(2, 7)
# link.remove(5)
# link.travel()
# # print(link.length())


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next


head = Node('head', None)
last = head
for i in range(5):
    node = Node('%s' % i, None)
    last.next = node
    last = node
# ######### 查看链表关系 ##########
print('原始链表信息为：')
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
print(head.next.next.next.next.next.value)


def reverse_linked_list(head):
    """
    链表逆置
    """
    if not head or not head.next:
        return head

    prev_node = None
    current_node = head
    next_node = head.next

    while True:
        current_node.next = prev_node
        if not next_node:
            break
        prev_node = current_node
        current_node = next_node
        next_node = current_node.next
    return current_node


new_head = reverse_linked_list(head)

print('逆置之后的链表')
print(new_head.value)
print(new_head.next.value)
print(new_head.next.next.value)
print(new_head.next.next.next.value)
print(new_head.next.next.next.next.value)
print(new_head.next.next.next.next.next.value)
