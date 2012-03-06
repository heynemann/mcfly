#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

import httplib2
from urllib import urlencode
import ujson

from domain import Catalogue, Document

class DocumentNotFoundError(RuntimeError):
    pass

class Connection(object):
    def __init__(self, username, password, host="http://localhost", port=4567):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = Network(self.host, self.port, self.username, self.password)

    def __assert_response(self, resp, content):
        if not resp or "status" not in resp or int(resp['status']) != 200:
            with file('/tmp/error.html', 'w') as error_file:
                error_file.write(content)
            raise RuntimeError('The connection failed (HTTP-%s with the following message: %s' % (resp['status'], content))

    def create_catalogue(self, name):
        resp, content = self.connection.post('catalogues/create', data={'name': name}, content_type='application/x-www-form-urlencoded')

        self.__assert_response(resp, content)
        catalogue_dict = ujson.loads(content)

        return Catalogue(name=catalogue_dict['name'],
                         count=int(catalogue_dict['documentCount']),
                         connection=self)

    def store_document(self, catalogue, document_body):
        resp, content = self.connection.post('%s/new' % catalogue.name, data={'message':ujson.dumps(document_body)}, content_type='application/x-www-form-urlencoded')
        self.__assert_response(resp, content)

        document_dict = ujson.loads(content)
        return Document(uri=document_dict['uri'],
                        id=document_dict['id'],
                        timestamp=document_dict['timestamp'],
                        body=document_dict['body'])

    def get_document(self, catalogue, id):
        resp, content = self.connection.get('%s/%s' % (catalogue.name, id))
        if resp and "status" in resp and int(resp['status']) == 404:
            raise DocumentNotFoundError('The document with id %s was not found int catalogue %s!' % (id, catalogue.name))
        self.__assert_response(resp, content)

        document_dict = ujson.loads(content)
        return self.new_document_for(document_dict)

    def new_document_for(self, document_dict):
        return Document(uri=document_dict['uri'],
                        id=document_dict['id'],
                        timestamp=document_dict['timestamp'],
                        body=document_dict['body'])

    def get_documents(self, catalogue):
        resp, content = self.connection.get('%s/documents' % catalogue.name)
        self.__assert_response(resp, content)

        documents = ujson.loads(content)

        loaded_documents = []
        for document in documents:
            loaded_documents.append(self.new_document_for(document))

        return loaded_documents

    def __getattr__(self, name):
        return self.create_catalogue(name)

class Network(object):
    def __init__(self, host, port, username, password):
        self.request = httplib2.Http(".cache")
        self.request.add_credentials(username, password)
        self.host = host
        self.port = port
        self.server = "%s:%s" % (self.host, self.port)

    def get(self, url, content_type='application/json'):
        resp, content = self.request.request(join(self.server, url),
            "GET",
            headers={'content-type':content_type})

        return resp, content

    def post(self, url, data={}, content_type='application/json'):
        body = urlencode(data)
        final_url = join(self.server, url)
        print "Posting to %s with body of %s" % (final_url, body)
        resp, content = self.request.request(final_url, "POST", body=body,
            headers={'content-type':content_type})

        return resp, content
