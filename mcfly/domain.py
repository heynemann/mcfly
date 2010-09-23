#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4

class Catalogue(object):
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection

    def post(self, document_body):
        return self.connection.post_document(self, document_body)

    def get(self, id):
        return self.connection.get_document(self, id)

class Document(object):
    def __init__(self, uri, id, timestamp, body):
        self.uri = uri
        self.id = id
        self.timestamp = timestamp
        self.body = body
