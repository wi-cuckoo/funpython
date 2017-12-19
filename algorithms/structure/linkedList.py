#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def set_value(self, val):
        self.value = val


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, val):
        node = Node(val)
        node.set_next(self.head)
        self.head = node

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == val:
                return current_node
            current_node = current_node.get_next()
        return current_node

    def remove(self, val):
        found = False
        previous = None
        current_node = self.head
        while current_node is not None and not found:
            if current_node.get_value() == val:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()
        if previous is None:
            self.head = current_node.get_next()
        else:
            previous.set_next(current_node.get_next())


if __name__ == '__main__':
    meta = [12, 'fuck', False, {'a': 3}]
    L = UnorderedList()
    for x in meta:
        L.add(x)

    L.remove(False)
    print L.size()
