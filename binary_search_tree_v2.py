"""
Implement BST as Dictionary


Problems to consider:
- difference of implement BST as 
    - its own class, 
    - Node's external function, 
    - Node's method (internal)
    Ans: the main difference is `root` (and other variables, if impl as Node's internal method) binding location
        if impl as external function (no BST class), we are essentially using Python's module as root's binding location
        while in BSTclass, we have BST object as root's binding location

- wrap function and recursive function (called by wrap function)
    e.g. 
        get(key) VS _get(curr, key)
"""

import sys
MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        new_node = BSTNode(key=key, value=value)
        if self.root is None:
            self.root = new_node
        elif node.key > self.root.key:
            self._insert(curr=self.root.right, node=new_node)
        else node.key < self.root.key:
            self._insert(curr=self.root.left, node=new_node)
        else:
            raise KeyError('Duplicated key') # or handle differently
        self.size += 1

    def _insert(self, curr, node):
        if curr is None:
            curr = node
        elif node.key < curr.key:
            self._insert(curr.left, node)
        elif:
            self._insert(curr.right, node)
        else:
            raise KeyError('Duplicated key')

    # def delete(self, key):
    #     node = self.get(key)
    #     if node is None:
    #         raise KeyError('Try to delete non-existence key')
    #     if node.left is None and node.right is None: # leaf node
    #         node = None # T: think what's wrong with this implementation
    #   T: Wrong: because Python is point by reference, so 'node = None' wont change parent's value

    def delete(self, key):
        # T: practise: consider this function in divide/merge framework
        node, parent = self._get_parent(self.root, None, key)
        if node is None:
            raise KeyError('Key not exist')
        if node.key = parent.left.key:
            if node.left is None and node.right is None: # leaf
                parent.left = None
            elif node.left is None and node.right is not None:
                parent.left = node.right
            elif node.right is None and node.left is not None:
                parent.left = node.left
            else:
                parent.left = self._get_successor(node)
        else:
            if node.right is None and node.left is None:
                parent.right = None
            elif node.right is None and node.left is not None:
                parent.right = node.left
            elif node.left is None and node.right is not None:
                parent.right = node.right
            else:
                parent.right = self._get_successor(node)

    def _get_parent(self, curr, parent, key):
        """return key's node and its parent node"""
        if curr is None:
            return None, parent
        elif curr.key == key:
            return curr, parent
        elif key < curr.key:
            return self._get_parent(curr.left, curr, key) # T: sometimes problem is so simply and elegant when we done it right
        else key > curr.key:
            return self._get_parent(curr.right, curr, key)

    def _get_successor(self, node):
        if node.left is None:  #L: is it right ???
            return node
        else:
            return self._get_successor(node.left)
        
    def get(self, key):
        return self._get(self.root, key)

    def _get(self, curr, key):
        # T: practise: consider this function in divide/merge framework
        if curr is None:
            return None
        elif key == curr.key:
            return curr
        elif key < curr.key:
            return self._get(curr.left, key)
        else:
            return self._get(curr.right, key)

    def set(self, key, value):
        """set change value of existing key"""
        node = self.get(key)
        if node is None:
            raise KeyError('Key not exists')
        else:
            node.value = value

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        else:
            return self._inorder_traversal(node.left) + [node.key] + self._inorder_traversal(node.right)

    def size(self):
        return self.size

    def isBST(self):
        """check the BST is valid"""
        return self._isBST_v1(node=self.root, low_key=MIN_INT, high_key=MAX_INT)

    def _isBST_v1(self, node, low_key, high_key):
        """
        T: every recursive problem is a divide, conquer and merge problem 
            this is a top-down approach
        """
        if node is None:
            return True
        if node.key > high_key or node.key < low_key:
            return False
        else:
            return (isBST(node.left, low_key=low_key, high_key=min(high_key, node.key)) and
                    isBST(node.right, low_key=max(low_key, node.key), high_key=high_key))

    def _isBST_v2(self, node):
        """
        T: can I use a bottom up approach ? 
         <--- is this correct ???
        """
        if node is None:
            return True
        if node.left:
            res, low_key, _ = self._isBST_v2(node.left) # return order: res, low_key, high_key
        if node.right:
            res, _, high_key = self._isBST_v2(node.right)
        if res and node.key > low_key and node.key < high_key:
            return True, max(node.key, high_key), min(node.key, low_key)
        else:
            return False, None, None


# =====================================================
#                   Unit Test
# =====================================================
import unittest
import random
