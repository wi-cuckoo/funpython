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

def infix2sufix(exp):
    ops = {'*': 3, '/': 3, '+': 1, '-': 1, '(': 0}
    suffix_exp = ''
    stack = Stack()
    for c in exp.split():
        if c in '0123456789':
            suffix_exp += c
        elif c == '(':
            stack.push(c)
        elif c == ')':
            op = stack.pop()
            while op != '(':
                suffix_exp += op
                op = stack.pop()
        else:
            while (not stack.is_empty()) and \
                (ops[stack.peek()] > ops[c]):
                suffix_exp += stack.pop()
            stack.push(c)

    while not stack.is_empty():
        suffix_exp += stack.pop()

    return suffix_exp

def cacl(sufix):
    def do_cal(num1, num2, op):
        if op == '*':
            return num1 * num2
        if op == '/':
            return num1 / num2
        if op == '+':
            return num1 + num2
        return num1 - num2

    stack = Stack()
    for c in sufix:
        if c in '0123456789':
            stack.push(int(c))
            continue
        num1 = stack.pop()
        num2 = stack.pop()
        stack.push(do_cal(num1, num2, c))
    return stack.pop()



if __name__ == '__main__':
    res = base_convert(255, 2)
    # print(res)
    sufix = infix2sufix('( 1 + 2 ) * ( 3 + 4 + 3 )')
    print(cacl(sufix))
