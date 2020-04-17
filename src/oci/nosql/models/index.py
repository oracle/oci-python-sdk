# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Index(object):
    """
    Information about an index.
    """

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Index.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Index object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Index.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Index.
        :type compartment_id: str

        :param table_name:
            The value to assign to the table_name property of this Index.
        :type table_name: str

        :param table_id:
            The value to assign to the table_id property of this Index.
        :type table_id: str

        :param keys:
            The value to assign to the keys property of this Index.
        :type keys: list[IndexKey]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Index.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Index.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'name': 'str',
            'compartment_id': 'str',
            'table_name': 'str',
            'table_id': 'str',
            'keys': 'list[IndexKey]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'compartment_id': 'compartmentId',
            'table_name': 'tableName',
            'table_id': 'tableId',
            'keys': 'keys',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._name = None
        self._compartment_id = None
        self._table_name = None
        self._table_id = None
        self._keys = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def name(self):
        """
        Gets the name of this Index.
        Index name.


        :return: The name of this Index.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Index.
        Index name.


        :param name: The name of this Index.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Index.
        Compartment Identifier.


        :return: The compartment_id of this Index.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Index.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this Index.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def table_name(self):
        """
        Gets the table_name of this Index.
        The name of the table to which this index belongs.


        :return: The table_name of this Index.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this Index.
        The name of the table to which this index belongs.


        :param table_name: The table_name of this Index.
        :type: str
        """
        self._table_name = table_name

    @property
    def table_id(self):
        """
        Gets the table_id of this Index.
        the OCID of the table to which this index belongs.


        :return: The table_id of this Index.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """
        Sets the table_id of this Index.
        the OCID of the table to which this index belongs.


        :param table_id: The table_id of this Index.
        :type: str
        """
        self._table_id = table_id

    @property
    def keys(self):
        """
        Gets the keys of this Index.
        A set of keys for a secondary index.


        :return: The keys of this Index.
        :rtype: list[IndexKey]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """
        Sets the keys of this Index.
        A set of keys for a secondary index.


        :param keys: The keys of this Index.
        :type: list[IndexKey]
        """
        self._keys = keys

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Index.
        The state of an index.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Index.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Index.
        The state of an index.


        :param lifecycle_state: The lifecycle_state of this Index.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Index.
        A message describing the current state in more detail.


        :return: The lifecycle_details of this Index.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Index.
        A message describing the current state in more detail.


        :param lifecycle_details: The lifecycle_details of this Index.
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
