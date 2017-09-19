#! /usr/bin/env python3
# -*- coding:utf-8 -*-


class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, node):
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, val):
        self.key = val

    def get_root_val(self):
        return self.key


def build_tree():
    t = BinaryTree('a')
    t.insert_left('b')
    t.get_left_child().insert_right('d')
    t.insert_right('c')
    t.get_right_child().insert_left('e')
    t.get_right_child().insert_right('f')
    return t


if __name__ == '__main__':
    tree = build_tree()
    print(tree.get_right_child().get_root_val())
