#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))

from mcfly import Connection

def test_connection():
    connection = Connection(username='admin', password='12345')
    assert connection.connection

def test_create_catalogue():
    connection = Connection(username='admin', password='12345')
    catalogue = connection.create_catalogue('test_catalogue_1')

    assert catalogue.name == "test_catalogue_1"
