class LinkedStack:
    def __init__(self):
        self.first = None
        self.n = 0

    class Node:
        def __init__(self, item=None, next=None):
            self.item = item
            self.next = next

    def push(self, item):
        self.first = self.Node(item, self.first)
        self.n += 1

    def pop(self):
        if self.n == 0:
            return None
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        return item

    def peek(self):
        return self.first.item

    def isEmpty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        current = self.first
        while current:
            yield current.item
            current = current.next

