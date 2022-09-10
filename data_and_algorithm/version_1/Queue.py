class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        return self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == []

    def size(self):
        return len(self.items)

