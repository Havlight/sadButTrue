class AVLNode(object):
    def __init__(self, data, l=None, r=None, p=None):
        self.data = data
        self.lChild = l
        self.rChild = r
        self.parent = p
        self.bf = 0

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rChild or self.lChild)

    def is_left_child(self):
        return self.parent and self.parent.lChild == self

    def is_right_child(self):
        return self.parent and self.parent.rChild == self


class AVLTree(object):
    def __init__(self, li=None):

        self.root = None
        self.size = 0
        if li:
            for data in li:
                self.put(data)

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.lChild)
            print(node.data)
            self.in_order_print(node.rChild)

    def find(self, data, node=None):
        if not node:
            node = self.root
        while node:
            if data < node.data:
                node = node.lChild
            elif data > node.data:
                node = node.rChild
            else:
                return node
        return None

    def find_min(self, node=None):
        if not node:
            min_node = self.root
        else:
            min_node = node

        while min_node.lChild:
            min_node = min_node.lChild
        return min_node

    def find_max(self, node=None):
        if not node:
            max_node = self.root
        else:
            max_node = node
        while max_node.rChild:
            max_node = max_node.rChild
        return max_node

    def find_succ(self, data):
        node = self.find(data)
        if node:
            return self._find_succ(node)
        else:
            return None

    def _find_succ(self, node: AVLNode):
        succ = None
        if node.rChild:
            succ = self.find_min(node.rChild)
        else:
            if node.parent:
                if node.is_left_child():
                    succ = node.parent
                else:
                    p = node.parent
                    p.rChild = None
                    succ = self._find_succ(p)
                    p.rChild = node
        return succ

    def find_prede(self, data):
        node = self.find(data)
        if node:
            return self._find_prede(node)
        else:
            return None

    def _find_prede(self, node: AVLNode):
        prede = None
        if node.rChild:
            prede = self.find_max(node)
        else:
            if node.parent:
                if node.is_right_child():
                    prede = node.parent
                else:
                    p = node.parent
                    p.lChild = None
                    prede = self._find_prede(p)
                    p.lChild = node
        return prede

    def put(self, data):
        if self.root is None:
            self.root = AVLNode(data=data)
        else:
            self._put(data, self.root)

    def _put(self, data, cur_node: AVLNode):
        if data == cur_node.data:
            return None
        elif data < cur_node.data:
            if cur_node.lChild:
                self._put(data, cur_node.lChild)
            else:
                cur_node.lChild = AVLNode(data, p=cur_node)
                self._put_update_bf(cur_node.lChild)
        else:
            if cur_node.rChild:
                self._put(data, cur_node.rChild)
            else:
                cur_node.rChild = AVLNode(data, p=cur_node)
                self._put_update_bf(cur_node.rChild)

    def _put_update_bf(self, node: AVLNode):
        if node.bf < -1 or node.bf > 1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.bf += 1
            else:
                node.parent.bf -= 1

            if node.parent.bf != 0:
                self._put_update_bf(node.parent)

    def rebalance(self, node: AVLNode):
        if node.bf < 0:
            if node.rChild.bf > 0:
                self.rotate_right(node.rChild)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.bf > 0:
            if node.lChild.bf < 0:
                self.rotate_left(node.lChild)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rot_root: AVLNode):
        newroot = rot_root.rChild
        newroot.parent = rot_root.parent

        rot_root.rChild = newroot.lChild
        if newroot.lChild:
            newroot.lChild.parent = rot_root

        if rot_root.is_root():
            self.root = newroot
        else:
            if rot_root.is_left_child():
                rot_root.parent.lChild = newroot
            else:
                rot_root.parent.rChild = newroot

        newroot.lChild = rot_root
        rot_root.parent = newroot

        rot_root.bf = rot_root.bf + 1 - min(0, newroot.bf)
        newroot.bf = newroot.bf + 1 + max(0, rot_root.bf)

    def rotate_right(self, rot_root: AVLNode):
        newroot = rot_root.lChild
        newroot.parent = rot_root.parent

        rot_root.lChild = newroot.rChild
        if rot_root.lChild:
            rot_root.lChild.parent = rot_root

        if rot_root.is_root():
            self.root = newroot
        else:
            if rot_root.is_left_child():
                rot_root.parent.lChild = newroot
            else:
                rot_root.parent.rChild = newroot

        newroot.rChild = rot_root
        rot_root.parent = newroot

        rot_root.bf = rot_root.bf - max(newroot.bf, 0) - 1
        newroot.bf = newroot.bf + min(rot_root.bf, 0) - 1


b = AVLTree([11, 10, 12, 56, 32, 10, 44, 89])
b.in_order_print(b.root)
print(b.root)
