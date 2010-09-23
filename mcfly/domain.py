#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4

class Catalogue(object):
    def __init__(self, name, count, connection):
        self.name = name
        self.count = count
        self.connection = connection

    def post(self, document_body):
        return self.connection.post_document(self, document_body)

    def get(self, id):
        return self.connection.get_document(self, id)

    def refresh(self):
        catalogue = self.connection.create_catalogue(self.name)
        self.name = catalogue.name
        self.count = catalogue.count

class Document(object):
    def __init__(self, uri, id, timestamp, body):
        self.uri = uri
        self.id = id
        self.timestamp = timestamp
        self.body = body
