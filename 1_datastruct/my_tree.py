class Node(object):
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myqueue = []

    def add(self, elem):
        node = Node(elem)
         
