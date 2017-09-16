#! /usr/bin/env python3
# -*- coding:utf-8 -*-


class Queue:

    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


def josephus(index):
    Q = Queue()
    for x in range(ord('A'), ord('Z')+1):
        Q.enqueue(chr(x))
    print(Q.queue)

    # pick a start pos to start counting
    from random import randint
    start = randint(1, Q.size())

    while start > 1:
        Q.enqueue(Q.dequeue())
        start -= 1

    pos = 1
    while Q.size() > 1:
        for x in range(index-1):
            Q.enqueue(Q.dequeue())
        Q.dequeue()
        print(Q.queue)

    return Q.dequeue()

if __name__ == '__main__':
    print(josephus(4))