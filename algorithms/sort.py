#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Sort(object):

    def __init__(self, method):
        self.method = method

    def do(self, l):
        if hasattr(self, self.method):
            return getattr(self, self.method)(l)
        return None

    def bubble(self, seq):
        l = [x for x in seq]
        n = len(l)
        while n > 0:
            for i in range(0, n-1):
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
            n -= 1
        return l

    def select(self, l):
        n = len(l)
        seq = [x for x in l]
        while n > 0:
            pos, max_el = 0, seq[0]
            for i in range(1, n):
                if max_el < seq[i]:
                    max_el, pos = seq[i], i
            seq[n-1], seq[pos] = seq[pos], seq[n-1]
            n -= 1
        return seq

    def insert(self, l):
        # copy the l
        seq = [x for x in l]
        n = len(seq)
        for i in range(1, n):
            el = seq[i]
            pos = i
            while pos > 0 and seq[pos-1] > el:
                seq[pos] = seq[pos-1]
                pos -= 1
            seq[pos] = el
        return seq


    def count(self, l, fn=lambda x: x):
        a, b = [], {}
        for x in l:
            val = fn(x)
            if b.get(val):
                b[val].append(x)
            else:
                b[val] = [x]

        for i in range(min(b), max(b) + 1, 1):
            if b.get(i) is None:
                continue
            a += b[i]
        return a

if __name__ == '__main__':
    sample = [20, 40, 30, 9, 50, 80, 70, 60, 110, 14]
    print('Bubble Sort: ', Sort('bubble').do(sample))
    print('select Sort: ', Sort('select').do(sample))
    print('insert Sort: ', Sort('insert').do(sample))
    print('Count Sort: ', Sort('count').do(sample))
