class ThreadNode(object):
    def __init__(self, data='#'):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.ltag = 0
        self.rtag = 0


class BinaryThreadTree(object):
    def __init__(self, data_list):
        self.data_list = data_list
        
        # 创建树的头结点
        self.HeadNode = ThreadNode()
        self.HeadNode.ltag = 0
        self.HeadNode.rtag = 0
        self.HeadNode.lchild = self.HeadNode
        self.PreNode = ThreadNode()

    def __CreateBinaryTree(self, root=None, pos=0):
        if pos >= len(self.data_list) or self.data_list[pos] == '#':
            # 递归结束条件
            return None
        else:
            root = ThreadNode(self.data_list[pos])
            # 递归建立左子树
            root.lchild = self.__CreateBinaryTree(root, 2 * pos + 1)
            # 递归建立右子树
            root.rchild = self.__CreateBinaryTree(root, 2 * pos + 2)
            return root

    def VisitBinaryTreeNode(self, RootNode):
        if RootNode.data != '#':
            print(RootNode.data, end=' ')

    def CreateInThread(self):
        RootNode = self.__CreateBinaryTree()
        if RootNode is None:
            self.HeadNode.lchild = self.HeadNode
        else:
            # lchild域的指针指向二叉树的根结点
            self.HeadNode.lchild = RootNode
            self.PreNode = self.HeadNode
            self.InThread(RootNode)
            # 处理最后一个结点
            self.PreNode.rtag = 1
            self.PreNode.rchild = self.HeadNode
            # rchild域的指针指向中序遍历时访问的最后一个结点
            self.HeadNode.rchild = self.PreNode

    def InThread(self, TreeNode):
        if TreeNode is not None:
            # 递归, 线索化左子树
            self.InThread(TreeNode.lchild)
            if TreeNode.lchild is None:
                # 当前结点没有左孩子
                # 将当前结点的ltag置为1, 表示lchild域指向的是前驱
                TreeNode.ltag = 1
                TreeNode.lchild = self.PreNode
            if self.PreNode.rchild is None:
                # 前驱结点没有右孩子
                # 将前驱结点的rtag置为1, 表示rchild域指向的是后继, 即当前的TreeNode
                self.PreNode.rtag = 1
                self.PreNode.rchild = TreeNode
            # 标记刚刚访问的结点为下个结点的前驱结点
            self.PreNode = TreeNode
            self.InThread(TreeNode.rchild)

    def InOrderThread(self):
        # TreeNode就是树的根结点
        TreeNode = self.HeadNode.lchild
        while TreeNode is not self.HeadNode:
            while TreeNode.ltag == 0:
                # 找到了树最左边的那个结点(不一定是叶结点)
                TreeNode = TreeNode.lchild
            self.VisitBinaryTreeNode(TreeNode)
            while TreeNode.rchild is not self.HeadNode and TreeNode.rtag == 1:
                # 线索后继
                TreeNode = TreeNode.rchild
                self.VisitBinaryTreeNode(TreeNode)
            # rtag=0就开始寻找右子树最左边那个结点
            TreeNode = TreeNode.rchild


if __name__ == '__main__':
    tree_obj = BinaryThreadTree('ABCDEF#')
    tree_obj.CreateInThread()
    tree_obj.InOrderThread()
