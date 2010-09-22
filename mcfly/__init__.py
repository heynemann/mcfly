#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

import httplib2
from urllib import urlencode
import simplejson

from domain import Catalogue

class Connection(object):
    def __init__(self, username, password, host="http://localhost", port=4567):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = Network(self.host, self.port, self.username, self.password)

    def __create_catalogue(self, name):
        resp, content = self.connection.post('catalogues/create', data=[('name', name)], content_type='application/x-www-form-urlencoded')

        if not resp or "status" not in resp or int(resp['status']) != 200:
            with file('/tmp/error.html', 'w') as error_file:
                error_file.write(content)
            raise RuntimeError('The connection failed (HTTP-%s with the following message: %s' % (resp['status'], content))
        catalogue_dict = simplejson.loads(content)

        return Catalogue(name=catalogue_dict['name'], connection=self)

    def __get_catalogue(self, name):
        pass

    def __getattr__(self, name):
        return self.__create_catalogue(name)

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
