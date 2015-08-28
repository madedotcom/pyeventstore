Python Eventstore Client
------------------------

Project homepage: `<https://github.com/madecom/pyeventstore>`_

Documentation: `<http://pyeventstore.readthedocs.org/>`_

Issue tracking: `<https://github.com/madecom/pyeventstore/issues>`_


What is this package for
------------------------

This work is a basic implementation of the
`Eventstore <https://geteventstore.com/>`_
`Protocol Buffers <https://developers.google.com/protocol-buffers/>`_ protocol 
over TCP.

We have to publish tons of events to eventstore ensure historical events. We
realised the eventstore TCP protocol would be much faster. The TCP protocol
seems much faster that HTTP so we decided to implement python client and CLI
for achieve our goals.

Nushell
-------

You have to produce a CSV file with exactly 3 columns: event id, event type,
event data. The CLI would be able to push those event to eventstore.

.. code:: bash

    $ cat events.csv
    ...
    "de305d54-75b4-431b-adb2-eb6b9e546014","test event","{\"data\": 12}"
    ...

    $ cat events.csv | escli --host localhost --stream=teststream

Installation
------------

.. code:: bash

    $ pip install pyeventstore

Dependencies
------------

This code is based on 
`protobuf 2.6.1 <https://pypi.python.org/pypi/protobuf/2.6.1>`_
which is currently available only for python 2.7 it follows that this package
is also available for that python version.

For more details please check the ``requirements.txt``.
