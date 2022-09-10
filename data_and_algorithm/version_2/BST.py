"""
二叉树由各节点链式构成，节点中保存了键、值、左节点指针、右节点指针、父节点指针等信息。
二叉树的遍历本质上为Node链上的遍历，因此可以利用__iter__和yeild方法实现遍历迭代器。
节点是否为根节点、叶节点或者中间节点（包括父节点和左右节点的情况）对于节点的递归非常重要，所以一并实现。
"""
import Stack


class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def __iter__(self):
        """
        通过__iter__实现中序遍历递归
        """
        if self:
            if self.hasLeftChild():
                for element in self.leftChild:
                    yield element
            yield self.key
            if self.hasRightChild():
                for element in self.rightChild:
                    yield element

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self

        if self.hasRightChild():
            self.rightChild.parent = self


"""
BTS的初始化和基本方法
"""


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        return self.get(item)

    def put(self, key, value):
        """
        插入新的节点,通过辅助函数_put实现
        """
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._put(self.root, key, value)
        self.size += 1

    def _put(self, node: TreeNode, key, value):
        """
        递归插入，直至找到合适的叶子节点位置
        """
        if key == node.key:
            node.value = value
        elif key < node.key:
            if not node.hasLeftChild():
                node.leftChild = TreeNode(key, value, parent=node)
            else:
                node = node.leftChild
                self._put(node, key, value)

        else:
            if not node.hasRightChild():
                node.rightChild = TreeNode(key, value, parent=node)
            else:
                node = node.rightChild
                self._put(node, key, value)

    def __contains__(self, item):
        if self.get(item):
            return True

        return False

    def get(self, key):
        """
        获取节点key对应的值，通过辅助函数_get实现
        """
        if not self.root:
            raise IndexError("empty binary tree!")
        else:
            res = self._get(self.root, key)
            if res:
                return res.value
            else:
                return None

    def _get(self, node, key):
        """
        递归查找，直至找到合适的叶子节点位置或者None
        """
        if node is None:
            return None
        elif node.key == key:
            return node
        elif node.key > key:
            return self._get(node.leftChild, key)
        else:
            return self._get(node.rightChild, key)

    def findMinValue(self):
        """
        通过调用_finMin返回整个二叉树中的最小值
        """

        node = self._findMin(self.root)
        return node.value

    def findMaxValue(self):
        """
        通过调用_finMin返回整个二叉树中的最小值
        """
        node = self._findMax(self.root)
        return node.value

    @staticmethod
    def _findMin(node: TreeNode):
        """
        二叉树中任意子树的最小值，必然在子树的最低左叶子节点上
        """
        if not node:
            return ValueError("Empty bts, not minial value!")
        else:
            while node.hasLeftChild():
                node = node.leftChild
            return node

    @staticmethod
    def _findMax(node: TreeNode):
        """
        二叉树中任意子树的最小值，必然在子树的最低右叶子节点上
        """
        if not node:
            return ValueError("Empty bts, not minial value!")
        else:
            while node.hasRightChild():
                node = node.rightChild
            return node

    def findSuccessor(self, key):
        node = self._get(self.root, key)
        if not node:
            return "No key in the bts, thus null result!"
        else:
            return self._findSuccessor(node)

    def _findSuccessor(self, node: TreeNode):
        """
        找到某节点的后继节点（整棵树中大于该节点value的最小节点），主要包括如下情况 :
        1) 若存在右子树，则必在右子树中，且为右子树的最左下角节点叶子节点
        2）若没有右子树，存在父节点，且为父节点的左子树，则后续节点即为父节点
        3）若没有右子树，存在父节点，但为父节点的右子树，则向上回溯（注意将父节点的右子树指针暂时关闭），直到找到为左节点的第一个父节点，然后按照情况2）
        """
        successor = None

        if node.hasRightChild():  # 情况1
            successor = self._findMin(node.rightChild)

        else:
            if node.parent:
                if node.isLeftChild():  # 情况2
                    successor = node.parent
                else:  # 情况3
                    parent = node.parent
                    parent.rightChild = None  # 暂时将父节点的右子树设为None
                    successor = self._findSuccessor(parent)
                    parent.rightChild = node  # 回复父节点的右子树

        if not successor:
            return "No successor!"

        else:
            return successor

    def findPredecessor(self, key):
        node = self._get(self.root, key)
        if not node:
            return "No key in the bts, thus null result!"
        else:
            return self._findPredecessor(node)

    def _findPredecessor(self, node: TreeNode):
        """
        找到某节点的前继节点（整棵树中小于该节点value的最大节点），主要包括如下情况 :
        1) 若存在左子树，则必在左子树中，且为左子树的最右下角节点叶子节点
        2）若没有左子树，存在父节点，且为父节点的右子树，则后续节点即为父节点
        3）若没有左子树，存在父节点，但为父节点的左子树，则向上回溯（注意将父节点的左子树指针暂时关闭），直到找到其为右节点的第一个父节点，然后按照情况2）
        """
        predecessor = None

        if node.hasLeftChild():  # 情况1
            predecessor = self._findMax(node.leftChild)

        else:
            if node.parent:
                if node.isRightChild():  # 情况2
                    predecessor = node.parent
                else:  # 情况3
                    parent = node.parent
                    parent.leftChild = None  # 暂时将父节点的右子树设为None
                    predecessor = self._findPredecessor(parent)
                    parent.leftChild = node  # 回复父节点的右子树

        if not predecessor:
            return "No successor!"

        else:
            return predecessor

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        """
        分类讨论：
        情况1：若为空树，返回错误
        情况2：若只有根，检验key是否一致，一致变为空数，不一致，返回错误
        情况3：若有多个节点：
            Step1：get到需要删除的节点，若没有返回错误，若有进入step2
            Step2：判断该节点子节点和父节点情况
                 1）若没有子节点，即为叶子节点，直接删除，同时根据其为左节点或右节点修改父节点状态
                 2）若只有左子树
                    2.1）若当前节点为根节点，删除当前节点，将其左子树设为根节点，；
                    2.2）若当前节点为左子树，删除当前节点，调整当前当前节点父节点左孩子引用与当前节点左子树父节点的引用关系
                    2.2）若当前节点为右子树，删除当前节点，调整当前当前节点父节点右孩子引用与当前节点左子树父节点的引用关系
                 3）若只有右子树
                    同样的三种情况，与若只有左子树镜像
                 4) 若存在左右子树： 找到后继节点(此处，必然为在后子树中找)，将后续节点替换改制，后续节点处最多不超过1棵子树（可反证法证明），然后按照上面1）——3)(不包括root的情况)进行后续的挪动
        """
        if not self.root:  # 空树
            raise KeyError("It is empty bts!")
        if self.size == 1:  # 只有根节点
            if self.root.key == key:
                self.root = None
                self.size = 0
            else:
                raise KeyError("No key in the bts!")

        else:
            node = self._get(self.root, key)
            if not node:  # 未找到key
                raise KeyError("No key in the bts!")

            elif node.isLeaf():  # 叶子节点,且肯定不为根节点，因此肯定有父节点
                if node.isLeftChild():
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None

            elif not node.hasBothChildren():  # 只有一个子树
                if node.hasLeftChild():  # 情况1：只有左子树
                    if node.isRoot():  # 情况1.1： 情况当前节点为根节点
                        node.replaceNodeData(node.leftChild.key, node.leftChild.value, node.leftChild.leftChild,
                                             node.leftChild.rightChild)
                    elif node.isLeftChild():  # 情况1.2： 当前节点为左节点
                        node.parent.leftChild = node.leftChild
                        node.leftChild.parent = node.parent

                    else:  # 情况1.3： 当前节点右节点
                        node.parent.rightChild = node.leftChild
                        node.leftChild.parent = node.parent

                else:  # 情况2：只有右子树
                    if node.isRoot():  # 情况2.1： 情况当前节点为根节点
                        node.replaceNodeData(node.rightChild.key, node.rightChild.value, node.rightChild.leftChild,
                                             node.rightChild.rightChild)
                    elif node.isLeftChild():  # 情况1.2： 当前节点为左节点
                        node.parent.leftChild = node.rightChild
                        node.rightChild.parent = node.parent

                    else:  # 情况1.3 当前节点为右节点
                        node.parent.rightChild = node.rightChild
                        node.rightChild.parent = node.parent

            else:  # 存在左右两棵子树，所以其后继节点必然为右子树上的最小值
                successor = self._findSuccessor(node)  # 该后继节点最多只有一棵子树
                if successor.isLeaf():  # 叶子节点
                    if successor.isLeftChild():
                        successor.parent.leftChild = None
                    else:
                        successor.parent.rightChild = None

                else:  # 左子树的最低层左节点，或者右子树的根节点
                    successor.parent.rightChild = successor.rightChild
                    successor.rightChild.parent = successor.parent

                node.replaceNodeData(successor.key, successor.value, node.leftChild, node.rightChild)

            self.size -= 1

    def __iter__(self):
        return self.root.__iter__()

    def traversal(self):
        """
        采用非递归的形式中序遍历
        """

        keys_list = []  # 存放节点key
        values_list = []  # 存放节点value
        stack = Stack.LinkedStack()
        current = self.root

        if current is None:
            return None

        while current or not stack.isEmpty():
            if current:
                stack.push(current)
                current = current.leftChild

            else:
                current = stack.pop()
                keys_list.append(current.key)
                values_list.append(current.value)
                current = current.rightChild

        return keys_list, values_list


class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def leftRotate(self, node):
        """
        左旋操作：（1）右孩子节点为新根节点，原根节点为左孩子节点；（2）若原右孩子节点本存在左孩子节点，则成为新左孩子节点的右孩子节点
        注意指针调整顺序、平衡因子的更新以及边界条件
        """
        newRoot = node.rightChild
        node.rightChild = newRoot.leftChild
        if newRoot.leftChild:
            newRoot.leftChild.parent = node

        if node.isLeftChild():
            newRoot.parent = node.parent
            node.parent.leftChild = newRoot
        elif node.isRightChild():
            newRoot.parent = node.parent
            node.parent.rightChild = newRoot
        else:
            newRoot.parent = None
            self.root = newRoot

        newRoot.leftChild = node
        node.parent = newRoot

        node.balanceFactor = node.balanceFactor - min(0, newRoot.balanceFactor) + 1
        newRoot.balanceFactor = newRoot.balanceFactor + max(node.balanceFactor, 0) + 1

    def rightRotate(self, node):
        """
        右旋操作:（1）左孩子节点为新根节点，原根节点为右孩子节点；（2）若原左孩子节点本存在右孩子节点，则成为新右孩子节点的左孩子节点
        注意指针调整顺序、平衡因子的更新以及边界条件
        """
        newRoot = node.leftChild
        node.leftChild = newRoot.rightChild
        if newRoot.rightChild:
            newRoot.rightChild.parent = node

        if node.isLeftChild():
            newRoot.parent = node.parent
            node.parent.leftChild = newRoot
        elif node.isRightChild():
            newRoot.parent = node.parent
            node.parent.rightChild = newRoot
        else:
            newRoot.parent = None
            self.root = newRoot

        newRoot.rightChild = node
        node.parent = newRoot

        node.balanceFactor = node.balanceFactor - max(newRoot.balanceFactor, 0) - 1
        newRoot.balanceFactor = newRoot.balanceFactor + min(0, node.balanceFactor) - 1

    def _put(self, node: TreeNode, key, value):
        """
        覆写添加节点操作，再原有基础上，更新平衡因子
        """
        if key == node.key:
            node.value = value
        elif key < node.key:
            if not node.hasLeftChild():
                node.leftChild = TreeNode(key, value, parent=node)
                self.put_updateBalanceFactor(node.leftChild)
            else:
                node = node.leftChild
                self._put(node, key, value)
        else:
            if not node.hasRightChild():
                node.rightChild = TreeNode(key, value, parent=node)
                self.put_updateBalanceFactor(node.rightChild)
            else:
                node = node.rightChild
                self._put(node, key, value)

    def put_updateBalanceFactor(self, node):
        """
        递归更新平衡因子并视情况进行子树旋转，其原则包括：
        （1）由当前节点向上回溯其父节点，视当前节点为左/右节点更新父节点的平衡因子；
        （2）终止条件包括：1）某祖先节点平衡因子调整为0;2）达到根节点；3）某祖先节点平衡因子调整为-2或2，进行旋转操作
        """
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.put_rotateTree(node)
            return

        if not node.isRoot():
            if node.isLeftChild():
                node.parent.balanceFactor += 1

            else:
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.put_updateBalanceFactor(node.parent)

    def put_rotateTree(self, node):
        """
        以某节点为根的子树的旋转操作，视该节点的平衡因子以及对应左孩子或右孩子节点的平衡因子选择对应的旋转方式
        因为触犯条件为平衡因子2或者-2所以在对应子树上必有孙子节点

        """
        if node.balanceFactor > 1:
            if node.leftChild.balanceFactor >= 0:  # 情况1：直接右旋
                self.rightRotate(node)

            else:  # 情况2：先左旋右子树，再右旋当前树
                self.leftRotate(node.rightChild)
                self.rightRotate(node)

        elif node.balanceFactor < -1:
            if node.rightChild.balanceFactor <= 0:  # 情况3： 直接左旋
                self.leftRotate(node)

            else:
                self.rightRotate(node.leftChild)  # 情况4： 先右旋左子树，再左旋当前树
                self.leftRotate(node)
        """
        其和BST的区别在于删除节点后，要对节点的父/祖先节点的平衡因子进行更新及子树的旋转
        注意删除操作和添加中平衡因子更新的方式和终止条件的区别
        """

    def delete(self, key):
        """
        AVL树的delete在BST基础上新增了平衡因子操作
        """
        if not self.root:  # 空树
            raise KeyError("It is empty bts!")
        if self.size == 1:  # 只有根节点
            if self.root.key == key:
                self.root = None
                self.size = 0
            else:
                raise KeyError("No key in the bts!")

        else:
            node = self._get(self.root, key)
            if not node:  # 未找到key
                raise KeyError("No key in the bts!")

            elif node.isLeaf():  # 叶子节点,且肯定不为根节点，因此肯定有父节点
                if node.isLeftChild():
                    node.parent.leftChild = None
                    self.delete_updateBalanceFactor(node)

                else:
                    node.parent.rightChild = None
                    self.delete_updateBalanceFactor(node)

            elif not node.hasBothChildren():  # 只有一个子树
                if node.hasLeftChild():  # 情况1：只有左子树,且子树只有1个根节点
                    if node.isRoot():  # 情况1.1： 情况当前节点为根节点
                        node.replaceNodeData(node.leftChild.key, node.leftChild.value, node.leftChild.leftChild,
                                             node.leftChild.rightChild)
                    elif node.isLeftChild():  # 情况1.2： 当前节点为左节点
                        node.parent.leftChild = node.leftChild
                        node.leftChild.parent = node.parent
                        self.delete_updateBalanceFactor(node)

                    else:  # 情况1.3： 当前节点右节点
                        node.parent.rightChild = node.leftChild
                        node.leftChild.parent = node.parent
                        self.delete_updateBalanceFactor(node)

                else:  # 情况2：只有右子树
                    if node.isRoot():  # 情况2.1： 情况当前节点为根节点
                        node.replaceNodeData(node.rightChild.key, node.rightChild.value, node.rightChild.leftChild,
                                             node.rightChild.rightChild)
                    elif node.isLeftChild():  # 情况1.2： 当前节点为左节点
                        node.parent.leftChild = node.rightChild
                        node.rightChild.parent = node.parent
                        self.delete_updateBalanceFactor(node)

                    else:  # 情况1.3 当前节点为右节点
                        node.parent.rightChild = node.rightChild
                        node.rightChild.parent = node.parent
                        self.delete_updateBalanceFactor(node)

            else:  # 存在左右两棵子树，所以其后继节点必然为右子树上的最小值
                successor = self._findSuccessor(node)  # 该后继节点最多只有一棵子树
                if successor.isLeaf():  # 叶子节点
                    if successor.isLeftChild():
                        successor.parent.leftChild = None
                    else:
                        successor.parent.rightChild = None

                else:  # 左子树的最低层左节点，或者右子树的根节点
                    successor.parent.rightChild = successor.rightChild
                    successor.rightChild.parent = successor.parent

                node.replaceNodeData(successor.key, successor.value, node.leftChild, node.rightChild)
                self.delete_updateBalanceFactor(successor)  # 物理本质上真正删除的是后继节点

            self.size -= 1

    def delete_updateBalanceFactor(self, node):

        if not node.isRoot():
            if node.isLeftChild():
                node.parent.balanceFactor -= 1

            else:
                node.parent.balanceFactor += 1

            if node.parent.balanceFactor == 0:
                self.delete_updateBalanceFactor(node.parent)

            if node.parent.balanceFactor < -1 or node.parent.balanceFactor > 1:
                self.delete_rotateTree(node.parent)
                self.delete_updateBalanceFactor(node.parent.parent)  # 经过旋转，当前节点的父节点变为了新的孩子节点

        if node.balanceFactor in [1, -1]:  # 主要顺序，要先更新父节点平衡因子
            return

    def delete_rotateTree(self, node):
        """
        以某节点为根的子树的旋转操作，视该节点的平衡因子选择对应的旋转方式
        因为BST删除节点而来，所以只有两种基本的旋转方式
        """
        if node.balanceFactor > 1:
            self.rightRotate(node)

        elif node.balanceFactor < -1:
            self.leftRotate(node)

