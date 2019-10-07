import queue

class Stack(object):

    def __init__(self):
        self.master_queue = queue.Queue()
        self.minor_queue = queue.Queue()

    def push(self, value):
        """
        入栈
        """
        self.master_queue.put(value)

    def pop(self):
        """
        出栈
        """
        if self.master_queue.qsize() == 0:
            return None

        while True:
            if self.master_queue.qsize() == 1:
                value = self.master_queue.get()
                break
            self.minor_queue.put(self.master_queue.get())
        # print(id(self.master_queue), id(self.minor_queue))
        self.master_queue, self.minor_queue = self.minor_queue, self.master_queue
        # print(id(self.master_queue), id(self.minor_queue))
        return value


obj = Stack()
obj.push('henry')
obj.push('echo')
obj.push('dean')

print(obj.pop())
print(obj.pop())
print(obj.pop())