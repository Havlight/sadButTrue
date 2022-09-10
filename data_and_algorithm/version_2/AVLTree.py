'''
TOPIC: AVL树
author: Blue
time: 2020-08-17
QQ: 2458682080
'''


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    # 利用递归插入
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    # 利用非递归插入
    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 如果p存在左孩子
                    p = p.lchild
                else:  # 如果p不存在左孩子
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    # 用递归查询
    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    # 不用递归查询
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 情况1: node是叶子节点
    def __remove_node_1(self, node):
        if not node.parent:  # 如果这个节点是根
            self.root = None
        if node == node.parent.lchild:  # 如果node是它父亲的左孩子
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    # 情况2.1: node只有一个左孩子
    def __remove_node_21(self, node):
        if not node.parent:  # 根结点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.lchild  # node删掉，node的左孩子给node的父亲作为左孩子
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    # 情况2.2: node只有一个右孩子
    def __remove_node_22(self, node):
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    # 删除
    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:  # node不存在
                return False
            # 情况1: node是叶结点
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            # 情况2.1: 只有左孩子
            elif not node.rchild:
                self.__remove_node_21(node)
            # 情况2.2: 只有右孩子
            elif not node.lchild:
                self.__remove_node_22(node)
            # 情况3: 两个孩子都有
            else:
                min_node = node.rchild
                # 找到右子树的最小节点
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node,这里min_node只有两种情况，要么是叶结点，要么就是只有右孩子
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

    # 前序遍历(先递归左子树，再递归右子树)
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历(先递归左子树，再访问自己，再递归右子树)
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    # 后续遍历(先递归左，后递归有，最后打印自己)
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    # 左旋
    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        # update balance factor
        p.bf = 0
        c.bf = 0
        return c

    # 右旋
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    # 右旋-左旋
    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.lchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # update balance factor
        if g.bf > 0:  # 插入g的左边
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:  # 插入g的右边
            p.bf = 0
            c.bf = 1
        else:  # 插入的是g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

        # 左旋-右旋

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        # 步骤1: 和BST一样，先插入
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 如果p存在左孩子
                    p = p.lchild
                else:  # 如果p不存在左孩子
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # node储存的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return

        # 步骤2: update balance factor
        while node.parent:
            # 传递是从左子树来的，左子树更沉了
            if node.parent.lchild == node:
                # 更新node.parent的bf -= 1
                if node.parent.bf < 0:  # 原来node.parent.bf == -1, 更新后变成-2
                    # 作旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 把n和g连起来
                elif node.parent.bf > 0:  # 原来node.parent.bf == -1, 更新后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0, 更新后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue

            # 传递是从右子树来的，右子树更沉了
            else:
                # 更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1, 更新后变成2
                    # 作旋转
                    # 看node哪边沉
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0:  # node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来
                elif node.parent.bf < 0:  # 原来node.parent.bf == -1, 更新后变成0
                    node.parent.bf = 0
                    break
                else:  # 原来node.parent.bf = 0, 更新后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 连接旋转后的子树
            n.parent = g
            if g:
                if node.parent == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
