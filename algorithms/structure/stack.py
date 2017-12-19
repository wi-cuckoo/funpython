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

    def peek(self):
        return self.stack[self.size() - 1]

    def size(self):
        return len(self.stack)


def example(data):
    stack = Stack()

    while data:
        stack.push(data % 2)
        data //= 2

    res = ''
    while not stack.is_empty():
        res += str(stack.pop())

    return res


def base_convert(num, base):
    digits = '0123456789ABCDEF'
    stack = Stack()
    while num:
        stack.push(digits[num % base])
        num //= base

    res = ''
    while not stack.is_empty():
        res += stack.pop()

    return res

if __name__ == '__main__':
    res = base_convert(255, 2)
    print(res)
