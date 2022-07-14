# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LimitAndUsage(object):
    """
    The limit and usage for a specific environment type, for example, production, development, or test.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LimitAndUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param limit:
            The value to assign to the limit property of this LimitAndUsage.
        :type limit: int

        :param usage:
            The value to assign to the usage property of this LimitAndUsage.
        :type usage: int

        """
        self.swagger_types = {
            'limit': 'int',
            'usage': 'int'
        }

        self.attribute_map = {
            'limit': 'limit',
            'usage': 'usage'
        }

        self._limit = None
        self._usage = None

    @property
    def limit(self):
        """
        **[Required]** Gets the limit of this LimitAndUsage.
        The limit of current environment.


        :return: The limit of this LimitAndUsage.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this LimitAndUsage.
        The limit of current environment.


        :param limit: The limit of this LimitAndUsage.
        :type: int
        """
        self._limit = limit

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this LimitAndUsage.
        The usage of current environment.


        :return: The usage of this LimitAndUsage.
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this LimitAndUsage.
        The usage of current environment.


        :param usage: The usage of this LimitAndUsage.
        :type: int
        """
        self._usage = usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
