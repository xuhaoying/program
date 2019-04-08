
class Node(object):
    def __init__(self, elem=1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    # If the left and right subtrees are not empty, join the queue and continue to judge.
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    # Depth first search
    def preorder(self, root):
        '''root -> left subtree -> right subtree'''
        if root is None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        '''left subtree -> root -> right subtree'''
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)
   
    def postorder(self, root):
        '''left subtree -> right subtree -> root'''
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    def breadth_travel(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel(tree.root)
    print("*" * 30)
    tree.preorder(tree.root)
    print("*" * 30)
    tree.inorder(tree.root)
    print("*" * 30)
    tree.postorder(tree.root)













