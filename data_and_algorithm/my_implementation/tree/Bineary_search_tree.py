class BST:
    class Node:
        def __init__(self, key, data, r_child=None, l_child=None):
            self.key = key
            self.data = data
            self.r_child = r_child
            self.l_child = l_child
            self.size = 1

    def __init__(self, li=None):
        self.root = None
        if li:
            for i, j in li:
                self.put(i, j)

    def put(self, key, data):
        self.root = self._put(self.root, key, data)

    def _put(self, node: Node, key, data):
        if not node: return self.Node(key, data)

        if key < node.key:
            node.l_child = self._put(node.l_child, key, data)
        elif key > node.key:
            node.r_child = self._put(node.r_child, key, data)
        else:
            node.data = data
        node.size = self.size_of(node.l_child) + self.size_of(node.r_child) + 1

        return node

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node: Node, key):
        if not node: return None

        if key < node.key:
            return self._get(node.l_child, key)
        elif key > node.key:
            return self._get(node.r_child, key)
        else:
            return node.data

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.l_child)
            print(node.data)
            self._inorder(node.r_child)

    def size_of(self, node):
        if node:
            return node.size
        else:
            return 0

    def min_node(self, node: Node):
        if not node.l_child: return node
        return self.min_node(node.l_child)

    def floor(self, key):
        r = self._floor(self.root, key)
        if r:
            return r.key
        return None

    def _floor(self, node: Node, key):
        if not node: return None

        if node.key == key:
            return node
        elif node.key > key:
            return self._floor(node.l_child, key)
        tmp = self._floor(node.r_child, key)
        if tmp:
            return tmp
        else:
            return node

    def del_min(self, node: Node):
        if not node.l_child: return node.r_child
        node.l_child = self.del_min(node.l_child)
        node.size = self.size_of(node.l_child) + self.size_of(node.r_child) + 1
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key):
        if not node: return None

        if key < node.key:
            node.l_child = self._delete(node.l_child, key)
        elif key > node.key:
            node.r_child = self._delete(node.r_child, key)
        else:
            if not node.r_child:
                return node.l_child
            elif not node.l_child:
                return node.r_child
            tmp = node
            node = self.min_node(node.r_child)
            node.r_child = self.del_min(tmp.r_child)
            node.l_child = tmp.l_child
        node.size = self.size_of(node.l_child) + self.size_of(node.r_child) + 1
        return node


if __name__ == '__main__':
    li = [(5, 121), (3, 445), (9, 456), (11, 123), (8, 656), (5, 13), (13, 586), (18, 53), (24, 63), (3, 23), (1, 0)]
    bst = BST(li=li)
    # bst.inorder()
    print(bst.get(1))
    bst.delete(1)
    print(bst.get(1)) 
