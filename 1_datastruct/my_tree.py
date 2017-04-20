class Node(object):
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):
        self.root = Node()

    def create(self,elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
        else:
            queue=[]
            treenode = self.root
            queue.append(treenode)
            while queue:
                treenode = queue.pop(0)
                if treenode.left == None:
                    treenode.left = node
                    return
                elif treenode.right == None:
                    treenode.right = node
                    return
                else:
                    queue.append(treenode.left)
                    queue.append(treenode.right)

    def preorder(self,root):
        if root == None:
            return
        print (root.elem)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print (root.elem)
        self.inorder(root.right)
    
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print (root.elem)

t=Tree()
t.create(1)
t.create(3)
t.create(2)
t.create(5)
t.create(7)
t.create(9)
print ('----------------')
t.preorder(t.root)
print ('----------------')
t.inorder(t.root)
print ('----------------')
t.postorder(t.root)
