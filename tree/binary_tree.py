
class BinaryTree:
    class BinaryTreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def __init__(self, L: list):
        self.head = self.level_order_create(L, 0)

    def level_order_create(self, L: list, pos: int):
        if(len(L) == 0):
            return self.BinaryTreeNode(None)
        root = self.BinaryTreeNode(L[pos])
        left_pos = 2*pos+1
        right_pos = 2*pos+2
        if(left_pos < len(L) and L[left_pos] != None):
            root.left = self.level_order_create(L, left_pos)
        if(right_pos < len(L) and L[right_pos] != None):
            root.right = self.level_order_create(L, right_pos)
        return root

    def pre_order_traversal(self):
        res = []
        self.__pre_order_traversal(self.head, res)
        return res

    def __pre_order_traversal(self, node: BinaryTreeNode, res: list):
        if(node == None):
            return
        res.append(node.val)
        self.__pre_order_traversal(node.left, res)
        self.__pre_order_traversal(node.right, res)

    def in_order_traversal(self):
        res = []
        self.__in_order_traversal(self.head, res)
        return res

    def __in_order_traversal(self, node: BinaryTreeNode, res: list):
        if(node == None):
            return
        self.__in_order_traversal(node.left, res)
        res.append(node.val)
        self.__in_order_traversal(node.right, res)

    def post_order_traversal(self):
        res = []
        self.__post_order_traversal(self.head, res)
        return res

    def __post_order_traversal(self, node: BinaryTreeNode, res: list):
        if(node == None):
            return
        self.__post_order_traversal(node.left, res)
        self.__post_order_traversal(node.right, res)
        res.append(node.val)

    def depth(self):
        return self.__get_depth(self.head)

    def __get_depth(self, node: BinaryTreeNode):
        if(node == None):
            return 0
        else:
            return 1 + max(self.__get_depth(node.left), self.__get_depth(node.right))


L = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
bt = BinaryTree(L)
print(bt.pre_order_traversal())
print(bt.in_order_traversal())
print(bt.post_order_traversal())
print(bt.depth())
