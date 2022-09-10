class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key

    def preOrder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preOrder()
        elif self.rightChild:
            self.rightChild.preOrder()


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getleftChild())
        preorder(tree.getRightChild())

