#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Pool
from mcfly import Connection, Catalogue

def f(i):
    conn = Connection("admin", "12345")
    return conn.store_document(Catalogue('test', 0, conn), { "docId": i})

def main():
    conn = Connection("admin", "12345")
    conn.create_catalogue('test')

    p = Pool(processes=5)
    p.map(f, range(10000))

if __name__ == '__main__':
    main()

