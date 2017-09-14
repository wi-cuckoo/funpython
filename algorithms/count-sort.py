#! /usr/bin/env python
# -*- coding:utf-8 -*-

import timeit


def count_sort(seq, fn=lambda x: x):
    a, b = [], {}
    for x in seq:
        val = fn(x)
        if b.get(val):
            b[val].append(x)
        else:
            b[val] = [x]

    for i in xrange(min(b), max(b)+1):
        if b.get(i) is None:
            continue
        a += b[i]
    return a

if __name__ == '__main__':
    example = [12, 4, 5, 12, 5] * 100000
    print count_sort(example)
