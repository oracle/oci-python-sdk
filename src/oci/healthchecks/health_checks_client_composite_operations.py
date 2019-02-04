# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci   # noqa: F401


class HealthChecksClientCompositeOperations(object):
    """
    This class provides a wrapper around :py:class:`~oci.healthchecks.HealthChecksClient` and offers convenience methods
    for operations that would otherwise need to be chained together. For example, instead of performing an action
    on a resource (e.g. launching an instance, creating a load balancer) and then using a waiter to wait for the resource
    to enter a given state, you can call a single method in this class to accomplish the same functionality
    """

    def __init__(self, client, **kwargs):
        """
        Creates a new HealthChecksClientCompositeOperations object

        :param HealthChecksClient client:
            The service client which will be wrapped by this object
        """
        self.client = client
