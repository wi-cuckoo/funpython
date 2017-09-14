#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Sort(object):

    def __init__(self, method):
        self.method = method

    def do(self, l):
        if hasattr(self, self.method):
            return getattr(self, self.method)(l)
        return None

    def bubble(self, l):
        return 'bubble sort'

    def select(self, l):
        return 'select sort'


if __name__ == '__main__':
    sample = [20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    print Sort('bubble').do(sample)
