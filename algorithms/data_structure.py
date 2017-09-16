#! /usr/bin/env python3
# -*- coding:utf-8 -*-


class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def example(self, data):
        while data:
            self.push(data % 2)
            data //= 2

        res = ''
        while not self.is_empty():
            res += str(self.pop())

        return res

if __name__ == '__main__':
    stack = Stack()
    print(stack.example(233))
    print(stack.is_empty())