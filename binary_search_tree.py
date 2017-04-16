

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_node(root, node): # not insert_value
    if root is None:
        root = node
    else:
        if root.value > node.value: # T: I don't feel the need for if root.left == None: ???
            insert_node(root.left, node)
        elif root.value < node.value:
            insert_node(root.right, node)

def delete_node(root, node):


def pre_order_traversal(root):


def in_order_traversal(root):


def post_order_traversal(root):







# class BST:
#     def __init__(self):
#         self.root = None

