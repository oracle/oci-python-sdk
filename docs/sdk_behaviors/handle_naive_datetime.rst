.. _handle-naive-datetime:

Handling naive datetimes
~~~~~~~~~~~~~~~~~~~~~~~~~~
For operations and models which accept a `datetime <https://docs.python.org/3.6/library/datetime.html>`__ object, if a naive
``datetime`` is passed (i.e. one without any ``tzinfo``) then the SDK will interpret the date and time as being UTC. This is
the equivalent of running the following code on the naive ``datetime``:

.. code-block:: pycon

    >>> import datetime
    >>> import pytz
    >>> my_naive_datetime = datetime.datetime(2001, 1, 1, 12, 30)
    >>> my_naive_datetime
    datetime.datetime(2001, 1, 1, 12, 30)
    >>> pytz.utc.localize(my_naive_datetime)
    datetime.datetime(2001, 1, 1, 12, 30, tzinfo=<UTC>)


For aware ``datetime`` objects (i.e. those with a ``tzinfo``), their timezone information will be used as-is.