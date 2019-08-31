1.  评判程序的优劣
    -   消耗计算机资源和执行效率
    -   计算算法执行的耗时(没有源码)
    -   时间复杂度(有实现源码)
2.  时间复杂度
    -   评判规则：量化算法执行的操作/执行步骤的数量
    -   原则：时间复杂度表达式中最有意义的项
3.  数据结构：数据的组织方式，解决的的是一组数据如何进行保存
4.  timeit计算程序的平均耗时

```python
from timeit import Timer
timer = Timer('test01', setup='from __main__ import test01')
# 执行次数,默认执行 10,000 次
sec = timer.timerit(1000)
print(sec)
```

DS

#### stack

1.  Stack()：构造方法
2.  push() / pop()
3.  peek()
4.  isEmpty
5.  size()

```python
class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
```

#### queue

1.  Queue()
2.  enqueue(item)
3.  dequeue(item)
4.  isEmpty()
5.  size()

```python
class Queue(object):
    
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self,item):
        return self.items.pop() if self.items else None
        
     def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
```

-   示例：烫手的山芋

```python
queue = Queue()
kids = ['A', 'B', 'C', 'D', 'E', 'F']

for kid in kids:
    queue.enqueue(kid)

while queue.size() > 1:
    for i in range(6):
        kid = queue.dequeue()
        queue.enqueue(kid)
     queue.dequeue()
    
print('获胜者是：', queue.dequeue())
```

#### 双端队列：Double-ended Queue

1.  Deque()
2.  addFront(item)
3.  addRear(item)
4.  removeFront()
5.  removeRear()
6.  isEmpty()
7.  size()

```python
class Deque(object):
    
    def __init__(self):
        self.items = []
    
    def addFront(self, item)
    	self.items.append(item)
    	
    def addRear(self, item)
    	self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop() if self.items else None
    
    def removeRear(self):
        return self.items.pop(0) if self.items else None
    	
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
```

-   示例：回文检查

```python
deque = Deque()
def isHuiWen(s):
    for ch in s:
        q.addFront(ch)

    flag = True
    for i in range(len(s) // 2):
        if deque.removeFront() != deque.removeRear():
            flag = False
            break
	return flag

print(isHuiWen('hello'))
```