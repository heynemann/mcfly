Introduction
------------

Mcfly is the library to query and update the Delorean database in Python.

Connection
----------

Connecting to the database is really simple::

    connection = Connection(username='admin', password='12345')
    connection.connect()

Creating a Catalogue
--------------------

Creating a catalogue is used with the create_catalogue command from the connection class::

    connection = Connection(username='admin', password='12345')
    connection.connect()
    catalogue = connection.create_catalogue('my_catalogue')

You can also retrieve a current catalogue using::

    catalogue = connection.get_catalogue('my_catalogue')

Posting a document
------------------

Given you have a catalogue posting a new document is as simple as::

    my_message = {
                    'first-name': 'Bernardo',
                    'last-name': 'Heynemann
                 }
    document = catalogue.post(my_message)

Getting a document
------------------

Getting a document by its id is as simple as::

    document = catalogue.get(1)
