class MyQueue(object):
    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def peek(self):
        if len(self.dequeue) is not 0:
            return self.dequeue[len(self.dequeue) - 1]
        else:
            return self.enqueue[0]

    def pop(self):
        if len(self.dequeue) is 0:
            while len(self.enqueue) is not 0:
                self.dequeue.append(self.enqueue[len(self.enqueue) - 1])
                self.enqueue = self.enqueue[:-1]

        self.dequeue = self.dequeue[:-1]

    def put(self, value):
        self.enqueue.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()