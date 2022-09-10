class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    class Node:
        def __init__(self, item=None, next=None):
            self.item = item
            self.next = next

    def isEmpty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def enqueue(self, item):
        oldlast = self.last
        self.last = self.Node(item)
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        old = self.first.item
        self.first = self.first.next
        self.n -= 1
        if self.isEmpty():
            self.last = None
        return old

    def __iter__(self):
        current = self.first
        while current:
            yield current.item
            current = current.next


