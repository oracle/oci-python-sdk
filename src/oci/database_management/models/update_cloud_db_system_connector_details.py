# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateCloudDbSystemConnectorDetails(object):
    """
    The details required to update a cloud DB system connector.
    """

    #: A constant which can be used with the connector_type property of a UpdateCloudDbSystemConnectorDetails.
    #: This constant has a value of "MACS"
    CONNECTOR_TYPE_MACS = "MACS"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateCloudDbSystemConnectorDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.UpdateCloudDbSystemMacsConnectorDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_type:
            The value to assign to the connector_type property of this UpdateCloudDbSystemConnectorDetails.
            Allowed values for this property are: "MACS"
        :type connector_type: str

        """
        self.swagger_types = {
            'connector_type': 'str'
        }
        self.attribute_map = {
            'connector_type': 'connectorType'
        }
        self._connector_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectorType']

        if type == 'MACS':
            return 'UpdateCloudDbSystemMacsConnectorDetails'
        else:
            return 'UpdateCloudDbSystemConnectorDetails'

    @property
    def connector_type(self):
        """
        **[Required]** Gets the connector_type of this UpdateCloudDbSystemConnectorDetails.
        The type of connector.

        Allowed values for this property are: "MACS"


        :return: The connector_type of this UpdateCloudDbSystemConnectorDetails.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this UpdateCloudDbSystemConnectorDetails.
        The type of connector.


        :param connector_type: The connector_type of this UpdateCloudDbSystemConnectorDetails.
        :type: str
        """
        allowed_values = ["MACS"]
        if not value_allowed_none_or_none_sentinel(connector_type, allowed_values):
            raise ValueError(
                f"Invalid value for `connector_type`, must be None or one of {allowed_values}"
            )
        self._connector_type = connector_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
