# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndexSummary(object):
    """
    Information about an index.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndexSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this IndexSummary.
        :type name: str

        :param keys:
            The value to assign to the keys property of this IndexSummary.
        :type keys: list[oci.nosql.models.IndexKey]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IndexSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this IndexSummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'name': 'str',
            'keys': 'list[IndexKey]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'keys': 'keys',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._name = None
        self._keys = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def name(self):
        """
        Gets the name of this IndexSummary.
        Index name.


        :return: The name of this IndexSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IndexSummary.
        Index name.


        :param name: The name of this IndexSummary.
        :type: str
        """
        self._name = name

    @property
    def keys(self):
        """
        Gets the keys of this IndexSummary.
        A set of keys for a secondary index.


        :return: The keys of this IndexSummary.
        :rtype: list[oci.nosql.models.IndexKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this IndexSummary.
        A set of keys for a secondary index.


        :param keys: The keys of this IndexSummary.
        :type: list[oci.nosql.models.IndexKey]
        """
        self._keys = keys

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IndexSummary.
        The state of an index.


        :return: The lifecycle_state of this IndexSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IndexSummary.
        The state of an index.


        :param lifecycle_state: The lifecycle_state of this IndexSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this IndexSummary.
        A message describing the current state in more detail.


        :return: The lifecycle_details of this IndexSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this IndexSummary.
        A message describing the current state in more detail.


        :param lifecycle_details: The lifecycle_details of this IndexSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
