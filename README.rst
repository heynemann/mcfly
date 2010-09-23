Introduction
============

Mcfly is the library to query and update the Delorean database in Python.

Models
======

Mcfly uses the following models to represent Delorean entities:

Catalogue
---------

A catalogue is a "branch" of the delorean database. It is where you store your documents. The catalogue model has the following properties::

    name - Corresponds to the name of the catalogue.
           This is immutable and is a part of the URI for your documents.
    count - Document count. This number represents how many documents this catalogue currently holds.

Document
--------

A document is a representation of something you stored in the database. The document model has the following properties::

    uri - The unique identifier for the document, preceded by the name of the catalogue.
    id - The unique identified for the document.
    timestamp - The time of creation of the document.
    body - The actual dictionary that represents the json that was sent to the database.

Operations
==========

Connection
----------

Connecting to the database is really simple::

    connection = Connection(username='admin', password='12345')

Creating a Catalogue
--------------------

Creating a catalogue is used with the create_catalogue command from the connection class::

    connection = Connection(username='admin', password='12345')
    catalogue = connection.my_catalogue #implicitly creates the catalogue

You can also retrieve a catalogue using::

    catalogue = connection.my_catalogue

Storing a document
------------------

Given you have a catalogue storing a new document in it, is as simple as::

    my_message = {
                    'first-name': 'Bernardo',
                    'last-name': 'Heynemann
                 }
    document = connection.my_catalogue.store(my_message)

Getting a document
------------------

Getting a document by its id is as simple as::

    document = connection.my_catalogue.get('23kr4092')

Getting all catalogue documents
-------------------------------

You can also retrieve all documents from a catalogue (in the order they were inserted), using::

    document = connection.my_catalogue.get_documents()
