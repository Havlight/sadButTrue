class BTree:
    def __init__(self,item = None):
        self.v = item
        self.r = None
        self.l = None

    def fromInput(self, node=None, cov=None):
        ch = input()
        if ch == '#':
            node = None
        else:
            if cov:
                ch = cov(ch)
            node = BTree(ch)
            self.fromInput(node.l, cov)
            self.fromInput(node.r, cov)
            return node

    def fromList(self, items):
        n = len(items)
        if n == 0:
            return None

        def inner(index=0):
            if n <= index or items[index] is None:
                return None

            node = BTree(items[index])
            node.l = inner(2 * index + 1)
            node.r = inner(2 * index + 2)
            return node

        return inner()

    def preOrder(self):
            print(self.v)
            if self.l:
                self.l.preOrder()
            if self.r:
                self.r.preOrder()

    def inOrder(self):
        if self.l:
            self.l.preOrder()
        print(self.v)
        if self.r:
            self.r.preOrder()
a = [1,2,3,4,5,6,7,8,9,10]
BTree().fromList(a).inOrder()