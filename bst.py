# This class implements a Binary Search Tree Class
# The binary search tree class will include functionality of
#   1. Insert a Node in the Tree.
#   2. Search for a Node in the Tree
#   3. Various traversals including in order, preorder and postorder traversals.
#
#  The binary search tree is made of class Node objects.
#    Each node has three members: key is an integer, left and right child point to nodes.
#    If left is None, then it means that the node has no left child.
#    If right is None then the node has no right child.


class Node:

    def __init__(self, my_key): # Constructor for the Node.
        self.key = my_key       # Set the key to my_key
        self.left = None        # Set left child to None
        self.right = None       # Set right child to None

    def insert(self, key_to_insert):
        if key_to_insert < self.key:
            if self.left == None:
                self.left = Node(key_to_insert)
            else:
                self.left.insert(key_to_insert)
        elif key_to_insert > self.key:
            if self.right == None:
                self.right = Node(key_to_insert)
            else:
                self.right.insert(key_to_insert)
        # NOTE: If key_to_insert equals my_key,
        #       then the node need should NOT be inserted in the tree.
        # REMOVE the assert below
        #assert False, 'Function insert not implemented yet.'

    def inorder_traversal(self, ret_list):
        if self.left != None:
            inorder_traversal(self.left, ret_list)
        ret_list.extend(self.key)
        if self.right != None:
            inorder_traversal(self.right, ret_list)
        # REMOVE the assert below
        #assert False, 'Function inorder_traversal not implemented yet'

    def get_depth(self):
        if self == None:
            return 0
        rightDepth = self.right.get_depth
        leftDepth = self.left.get_depth
        if leftDepth < rightDepth:
            return rightDepth + 1
        else:
            return leftDepth + 1
        #   Depth of a tree with no children is 1.
        #   Otherwise, depth = 1 + max(depth(left subtree), depth(right subtree))
        # REMOVE the assert below
        #assert False, 'Function get_depth not implemented yet'

    def key_exists(self, key_to_find):
        if self.key == key_to_find:
            return True
        elif self.key > key_to_find:
            if self.left == None:
                return False
            else:
                self.left.key_exists(key_to_find)
        else:
            if self.right == None:
                return False
            else:
                self.right.key_exists(key_to_find)
        # return True if the key_to_find is already in the tree,
        #   otherwise return False
        # REMOVE the assert below
        #assert False, ' Function find not implemented yet'

if __name__ == '__main__':
    print('Please do not call this file directly.')
    print('To run autograder script: please call the test_bst.py')