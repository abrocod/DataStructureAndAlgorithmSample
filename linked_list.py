

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set(self, data):
        self.data = data

    def get(self):
        return self.data

    def next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_length(self):
        length = 0
        curr = self.head
        if curr:
            curr = curr.next
            length += 1
        return length

    def get_length_2(self):
        return self.length

    def get_length_3(self):
        def get_node_length(self, node):
            if node is None:
                return 0
            else:
                return 1 + get_node_length(node.next)
        return get_node_length(self.head)

    def insert(self, data, index):
        # assume starting index is 0
        new_node = Node(data)
        import pdb; pdb.set_trace()
        if index > self.length or index < 0:
            raise IndexError("Invalid insertion index")
        elif index == 0:
            # in order to insert, we need curr to stay ahead of index. 
            # So insert at head must be a special case
            tmp = self.head
            self.head = new_node
            new_node.next = tmp
            self.length += 1
        else:
            curr = self.head
            count = 0 # T: this is basic trick in linkedlist: use count to represent curr's index (sync their movement)
                        # T: therefore reduce thinking process to array-like
            if count < index - 1: # we want curr to stop at one node before insert position
                count += 1
                curr = curr.next # TODO: use while 
            else:
                # the edge case of index=self.length is automatically handled 
                tmp = curr.next
                curr.next = new_node
                new_node.next = tmp
                self.length += 1

    def append(self, data):
        # append data in the end
        new_node = Node(data)
        curr = self.head
        if curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, index):
        if index >= self.length or index < 0:
            # if length is 5, index=5 is an empty position (index start at 0)
            # this also handle case like empty linkedlist 
            raise IndexError('Invalid index')
        elif index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            count = 0
            if count < index - 1:  # TODO: change to while .... 
                curr = curr.next
                count += 1 # T: again, make sure count relect the curr's index (allow us to think like array)
            else:
                curr.next = curr.next.next # T: need to make sure curr.next exist 
                                            # (which is true based on index >= self.length)

    def get(self, index):
        """
        T: it is good design to:
            - make sure curr and count are sync, so that count represent the index of curr
            - if index starts at 0, then set count = 0
        """
        if index >= self.length or index < 0:
            raise IndexError('Invalid Index')
        curr = self.head
        count = 0
        while count != index:
            curr = curr.next
            count += 1
        return curr.data

    def set(self, index, value):
        pass

    def print_linkedlist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


# ==============================================================
# Unit Test
# ==============================================================

import unittest
import random

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.insert(5, 0)
        self.ll.insert(7, 1)
        self.ll.insert(4, 2)

    def testLength(self):
        self.assertEqual(self.ll.get_length(), 3)

    def testInsertEnd(self):
        self.ll.insert(9, 3)        
        self.assertEqual(self.ll.get(3), 9)

    def testInsertInvalid(self):
        self.assertRaises(IndexError, self.ll.insert(10, 5))

    def testInsertBeg(self):
        self.ll.insert(100, 0)
        self.assertEqual(self.ll.get(0), 100)

    def testInsertMid(self):
        self.ll.insert('a', 2)
        self.assertEqual(self.ll.get(2), 'a')

    def testDelete(self):
        # current ll: 100, 5, 'a', 7, 4, 9
        self.assertEqual(self.ll.get_length(), 6)
        self.assertEqual(sefl.ll.get(0), 100)
        self.ll.delete(0)
        self.assertEqual(self.ll.get(0), 5)
        self.assertEqual(self.ll.get_length(), 5)

        self.assertEqual(self.ll.get(3), 4)
        self.ll.delete(3)
        self.assertEqual(self.ll.get(3), 9)
        self.assertEqual(self.ll.get_length(), 4)



if __name__ == "__main__":
    unittest.main()





