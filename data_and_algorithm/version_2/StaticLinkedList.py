class staticLinkedList:
    def __init__(self, size=100):
        self.space = [self.Node(i + 1) for i in range(size)]
        self.space[size - 1].cur = 0
        self.maxSize = size

    class Node:
        def __init__(self, cur=0, item=None):
            self.cur = cur
            self.item = item

    def getCur(self):
        i = self.space[0].cur
        if i:
            self.space[0].cur = self.space[i].cur
        return i

    def __len__(self):
        c = 0
        k = self.space[self.maxSize - 1].cur
        while j := self.space[k].item:
            k = self.space[k].cur
            c += 1
        return c

    def insert(self, i, item):
        k = self.maxSize - 1
        # if i < 1 or i > len(self) + 1:
        #     return False
        j = self.getCur()
        if j:
            self.space[j].item = item
            for _ in range(1, i):
                k = self.space[k].cur
            self.space[j].cur = self.space[k].cur
            self.space[k].cur = j
            return True
        else:
            return False

    def remove(self, i):
        k = self.maxSize - 1
        for _ in range(1, i):
            k = self.space[k].cur
        j = self.space[k].cur
        self.space[k].cur = self.space[j].cur
        self._remove(j)
        return True

    def _remove(self, k):
        self.space[k].cur = self.space[0].cur
        self.space[0].cur = k

    def __iter__(self):
        l = self.space[self.maxSize - 1].cur
        while l:
            yield self.space[l].item
            l = self.space[l].cur
