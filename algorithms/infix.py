#! /usr/bin/env python
# -*- coding:utf-8 -*-

from structure.stack import Stack

prece = {
	'*': 3,
	'/': 3,
	'+': 2,
	'-': 2,
	'(': 1
}

def infix2postfix(exp):
	opstack = Stack()
	items = exp.split(' ')
	res = list()

	for item in items:
		if item not in '+-*/()':
			res.append(item)
		elif item == '(':
			opstack.push(item)
		elif item == ')':
			o = opstack.pop()
			while o != '(':
				res.append(o)
				o = opstack.pop()
		else:
			while not opstack.is_empty() and prece[opstack.peek()] >= prece[item]:
				res.append(opstack.pop())
			opstack.push(item)

	while not opstack.is_empty():
		res.append(opstack.pop())

	return ' '.join(res)

if __name__ == '__main__':
	exp = 'A * B - C'
	print infix2postfix(exp)
