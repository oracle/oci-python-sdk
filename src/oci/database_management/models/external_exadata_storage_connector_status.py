# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataStorageConnectorStatus(object):
    """
    The status of a Exadata storage server connector.
    """

    #: A constant which can be used with the status property of a ExternalExadataStorageConnectorStatus.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a ExternalExadataStorageConnectorStatus.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataStorageConnectorStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataStorageConnectorStatus.
        :type id: str

        :param status:
            The value to assign to the status property of this ExternalExadataStorageConnectorStatus.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_message:
            The value to assign to the error_message property of this ExternalExadataStorageConnectorStatus.
        :type error_message: str

        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str',
            'error_message': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'error_message': 'errorMessage'
        }

        self._id = None
        self._status = None
        self._error_message = None

    @property
    def id(self):
        """
        Gets the id of this ExternalExadataStorageConnectorStatus.
        The `OCID`__ of the Exadata storage connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalExadataStorageConnectorStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalExadataStorageConnectorStatus.
        The `OCID`__ of the Exadata storage connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalExadataStorageConnectorStatus.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ExternalExadataStorageConnectorStatus.
        The connection status of the connector.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExternalExadataStorageConnectorStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExternalExadataStorageConnectorStatus.
        The connection status of the connector.


        :param status: The status of this ExternalExadataStorageConnectorStatus.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ExternalExadataStorageConnectorStatus.
        The error message indicating the reason for failure or `null` if the connection was successful.


        :return: The error_message of this ExternalExadataStorageConnectorStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ExternalExadataStorageConnectorStatus.
        The error message indicating the reason for failure or `null` if the connection was successful.


        :param error_message: The error_message of this ExternalExadataStorageConnectorStatus.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
