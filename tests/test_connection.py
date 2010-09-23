#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))
from uuid import uuid4

from mcfly import Connection

def test_connection():
    connection = Connection(username='test', password='test')
    assert connection.connection

def test_create_catalogue():
    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_1

    assert catalogue.name == "test_catalogue_1"

def test_create_catalogue_twice_returns_same_catalogue():
    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_2
    catalogue = connection.test_catalogue_2

    assert catalogue.name == "test_catalogue_2"

def test_store_document():
    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_3
    document_body = {
        'name': 'Bernardo',
        'family_name': 'Heynemann',
        'male': True
    }
    document = catalogue.store(document_body)

    assert document.uri.startswith('/test_catalogue_3/'), document.uri
    assert len(document.id) == 8, len(document.id)
    assert sorted(document.body.keys()) == sorted(document_body.keys())

def test_get_document_by_uri():
    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_4
    document_body = {
        'name': 'Bernardo',
        'family_name': 'Heynemann',
        'male': True
    }
    document = catalogue.store(document_body)

    retrieved_document = catalogue.get(document.id)
    assert retrieved_document.uri == document.uri
    assert retrieved_document.id == document.id
    assert retrieved_document.body == document.body

def test_get_catalogue_count():
    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_5
    document_body = {
        'name': 'Bernardo',
        'family_name': 'Heynemann',
        'male': True
    }
    document = catalogue.store(document_body)
    document = catalogue.store(document_body)

    catalogue.refresh()

    assert catalogue.count == 2

def test_get_catalogue_documents():

    connection = Connection(username='test', password='test')
    catalogue = connection.test_catalogue_6
    document_body = {
        'name': 'Bernardo',
        'family_name': 'Heynemann',
        'male': True
    }
    document_a = catalogue.store(document_body)

    document_body_b = {
        'name': 'Aline',
        'family_name': 'Lucena',
        'male': False
    }
    document_b = catalogue.store(document_body_b)

    documents = catalogue.get_documents()

    assert documents[0].uri == document_a.uri
    assert documents[1].uri == document_b.uri

