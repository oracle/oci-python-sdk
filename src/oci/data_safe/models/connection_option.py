# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionOption(object):
    """
    Types of connection supported by Data Safe.
    """

    #: A constant which can be used with the connection_type property of a ConnectionOption.
    #: This constant has a value of "PRIVATE_ENDPOINT"
    CONNECTION_TYPE_PRIVATE_ENDPOINT = "PRIVATE_ENDPOINT"

    #: A constant which can be used with the connection_type property of a ConnectionOption.
    #: This constant has a value of "ONPREM_CONNECTOR"
    CONNECTION_TYPE_ONPREM_CONNECTOR = "ONPREM_CONNECTOR"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionOption object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.PrivateEndpoint`
        * :class:`~oci.data_safe.models.OnPremiseConnector`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this ConnectionOption.
            Allowed values for this property are: "PRIVATE_ENDPOINT", "ONPREM_CONNECTOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        """
        self.swagger_types = {
            'connection_type': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType'
        }

        self._connection_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'PRIVATE_ENDPOINT':
            return 'PrivateEndpoint'

        if type == 'ONPREM_CONNECTOR':
            return 'OnPremiseConnector'
        else:
            return 'ConnectionOption'

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this ConnectionOption.
        The connection type used to connect to the database. Allowed values:
        - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
        - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe.

        Allowed values for this property are: "PRIVATE_ENDPOINT", "ONPREM_CONNECTOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_type of this ConnectionOption.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this ConnectionOption.
        The connection type used to connect to the database. Allowed values:
        - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
        - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe.


        :param connection_type: The connection_type of this ConnectionOption.
        :type: str
        """
        allowed_values = ["PRIVATE_ENDPOINT", "ONPREM_CONNECTOR"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            connection_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_type = connection_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
