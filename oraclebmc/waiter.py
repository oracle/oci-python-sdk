# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import time

from .exceptions import MaximumWaitTimeExceeded, WaitUntilNotSupported


def wait_until(client, response, property, state, max_interval_seconds=30, max_wait_seconds=1200):
    """Wait until the value of the given property in the response data has the given value.

    This will block the current thread until either the
    the desired state or the maximum wait time is reached. This is only
    supported for responses resulting from GET operations. A typical use
    case is to wait on an instance until it is in a running state.

    Although this can be run on any property of the data resulting from any
    GET operation, the most common use case is to check state properties on
    operations that GET a single object.

    The wait will poll at an increasing interval up to 'max_interval_seconds'
    for a maximum total time of 'max_wait_seconds'. If the maximum time
    is exceeded, then it will raise a MaximumWaitTimeExceededError.

    On successful completion the final Response object will be returned. The
    original Response object will not be altered.

    If any responses result in an error, then the error will be thrown as normal
    resulting in the wait being aborted.

    :param client: A Response object resulting from a GET operation.
    :param response: A Response object resulting from a GET operation.
    :param property: A string with the name of the property from the response data to evaluate.
        For example, 'state'.
    :param state: The value of the property that will indicate successful completion of the wait.
        Type corresponds to the property type.
    :param max_interval_seconds: (optional) The maximum interval between queries, in seconds.
        Defaults to 30 seconds.
    :param max_wait_seconds: (optional) The maximum time to wait, in seconds.
        Defaults to 1200 seconds.
    :return: The final response, which will contain the property in the specified state.
    """

    if response.request.method.lower() != 'get':
        raise WaitUntilNotSupported('wait_until is only supported for get operations.')
    if not hasattr(response.data, property):
        raise ValueError('Response data does not contain the given property.')

    sleep_interval_seconds = 1
    start_time = time.time()

    while True:
        if getattr(response.data, property) == state:
            return response

        elapsed_seconds = (time.time() - start_time)

        if elapsed_seconds + sleep_interval_seconds > max_wait_seconds:
            if max_wait_seconds <= elapsed_seconds:
                raise MaximumWaitTimeExceeded('Maximum wait time has been exceeded.')

        time.sleep(sleep_interval_seconds)

        # Double the sleep each time up to the maximum.
        sleep_interval_seconds = min(sleep_interval_seconds * 2, max_interval_seconds)

        response = client.base_client.request(response.request)
