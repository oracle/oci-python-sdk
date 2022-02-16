# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AggregatorSummary(object):
    """
    A summary type containing information about the object's aggregator including its type, key, name and description.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AggregatorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AggregatorSummary.
        :type type: str

        :param key:
            The value to assign to the key property of this AggregatorSummary.
        :type key: str

        :param name:
            The value to assign to the name property of this AggregatorSummary.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this AggregatorSummary.
        :type identifier: str

        :param description:
            The value to assign to the description property of this AggregatorSummary.
        :type description: str

        """
        self.swagger_types = {
            'type': 'str',
            'key': 'str',
            'name': 'str',
            'identifier': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'key': 'key',
            'name': 'name',
            'identifier': 'identifier',
            'description': 'description'
        }

        self._type = None
        self._key = None
        self._name = None
        self._identifier = None
        self._description = None

    @property
    def type(self):
        """
        Gets the type of this AggregatorSummary.
        The type of the aggregator.


        :return: The type of this AggregatorSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AggregatorSummary.
        The type of the aggregator.


        :param type: The type of this AggregatorSummary.
        :type: str
        """
        self._type = type

    @property
    def key(self):
        """
        Gets the key of this AggregatorSummary.
        The key of the aggregator object.


        :return: The key of this AggregatorSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AggregatorSummary.
        The key of the aggregator object.


        :param key: The key of this AggregatorSummary.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this AggregatorSummary.
        The name of the aggregator.


        :return: The name of this AggregatorSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AggregatorSummary.
        The name of the aggregator.


        :param name: The name of this AggregatorSummary.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this AggregatorSummary.
        The identifier of the aggregator.


        :return: The identifier of this AggregatorSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this AggregatorSummary.
        The identifier of the aggregator.


        :param identifier: The identifier of this AggregatorSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def description(self):
        """
        Gets the description of this AggregatorSummary.
        The description of the aggregator.


        :return: The description of this AggregatorSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AggregatorSummary.
        The description of the aggregator.


        :param description: The description of this AggregatorSummary.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
