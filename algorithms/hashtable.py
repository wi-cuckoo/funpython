#! /usr/bin/env python
# -*- coding:utf-8 -*-


class HashTable():

    def __init__(self, length):
        self.size = length
        self.slots = [None] * length
        self.values = [None] * length

    def __setitem__(self, key, val):
        self.__put(key, val)

    def __getitem__(self, key):
        return self.__get(key)

    # reminder
    def __hash_it(self, key, rehash=False):
        if rehash:
            key += 1
        return key % self.size

    def __put(self, key, val):
        slot = self.__hash_it(key)

        def put_into_slots(k, v, sl):
            if self.slots[sl] is not None and self.slots[sl] != k:
                return False

            if self.slots[sl] is None:
                self.slots[sl] = k
                self.values[sl] = v
            else:
                self.values[sl] = v
            return True

        res = put_into_slots(key, val, slot)
        while not res:
            slot = self.__hash_it(slot, True)
            res = put_into_slots(key, val, slot)

    def __get(self, key):
        slot = self.__hash_it(key)
        val = None
        while self.slots[slot] is not None:
            if self.slots[slot] == key:
                val = self.values[slot]
                break
            else:
                slot = self.__hash_it(slot, True)

        return val

if __name__ == '__main__':
    ht = HashTable(12)
    ht[12] = 'cat'
    ht[23] = 'dog'
    ht[26] = 'fish'
    ht[13] = 'bird'

    print ht[23]
