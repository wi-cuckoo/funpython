#! /usr/bin/env python
# -*- coding:utf-8 -*-

from random import randrange


def randomDAG(nodes):
    n = len(nodes)
    DAG = {}

    for i in xrange(n):
        node = nodes[i]
        if DAG.get(node) is None:
            DAG[node] = []
        if i == n-1:
            continue
        DAG[node].append(nodes[randrange(i+1, n)])
    return DAG

if __name__ == '__main__':
    meta = ['a', 'c', 'd', 'g', 'f', 'k', 's', 'e']
    print randomDAG(meta)
