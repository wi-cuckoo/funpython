#! /usr/bin/env python
# -*- coding:utf-8 -*-

from random import randint
from copy import deepcopy


def random_sample():
    sample = []
    sample_x = [randint(x, 80) for x in xrange(20)]
    for x in sample_x:
        sample.append((x, randint(x+10, 90)))

    return sample


def sort_y(a, b):
    if a[1] > b[1]:
        return 1
    if a[1] == b[1]:
        return 0
    return -1

if __name__ == '__main__':
    sample = random_sample()
    sample.sort()

    S = {}
    while sample:
        x_n = sample.pop()
        S[x_n] = []
        for x_i in sample:
            if x_i[1] >= x_n[1]:
                S[x_n].append(x_i)

    print S
