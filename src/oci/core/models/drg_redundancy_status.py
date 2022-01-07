# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRedundancyStatus(object):
    """
    The redundancy status of the DRG. For more information, see
    `Redundancy Remedies`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Network/Troubleshoot/drgredundancy.htm
    """

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_AVAILABLE"
    STATUS_NOT_AVAILABLE = "NOT_AVAILABLE"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "REDUNDANT"
    STATUS_REDUNDANT = "REDUNDANT"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_SINGLE_IPSEC"
    STATUS_NOT_REDUNDANT_SINGLE_IPSEC = "NOT_REDUNDANT_SINGLE_IPSEC"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT"
    STATUS_NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT = "NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_MULTIPLE_IPSECS"
    STATUS_NOT_REDUNDANT_MULTIPLE_IPSECS = "NOT_REDUNDANT_MULTIPLE_IPSECS"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS"
    STATUS_NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS = "NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_MIX_CONNECTIONS"
    STATUS_NOT_REDUNDANT_MIX_CONNECTIONS = "NOT_REDUNDANT_MIX_CONNECTIONS"

    #: A constant which can be used with the status property of a DrgRedundancyStatus.
    #: This constant has a value of "NOT_REDUNDANT_NO_CONNECTION"
    STATUS_NOT_REDUNDANT_NO_CONNECTION = "NOT_REDUNDANT_NO_CONNECTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRedundancyStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DrgRedundancyStatus.
        :type id: str

        :param status:
            The value to assign to the status property of this DrgRedundancyStatus.
            Allowed values for this property are: "NOT_AVAILABLE", "REDUNDANT", "NOT_REDUNDANT_SINGLE_IPSEC", "NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT", "NOT_REDUNDANT_MULTIPLE_IPSECS", "NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS", "NOT_REDUNDANT_MIX_CONNECTIONS", "NOT_REDUNDANT_NO_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'id': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status'
        }

        self._id = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this DrgRedundancyStatus.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DrgRedundancyStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgRedundancyStatus.
        The `OCID`__ of the DRG.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DrgRedundancyStatus.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """
        Gets the status of this DrgRedundancyStatus.
        The redundancy status of the DRG.

        Allowed values for this property are: "NOT_AVAILABLE", "REDUNDANT", "NOT_REDUNDANT_SINGLE_IPSEC", "NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT", "NOT_REDUNDANT_MULTIPLE_IPSECS", "NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS", "NOT_REDUNDANT_MIX_CONNECTIONS", "NOT_REDUNDANT_NO_CONNECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DrgRedundancyStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DrgRedundancyStatus.
        The redundancy status of the DRG.


        :param status: The status of this DrgRedundancyStatus.
        :type: str
        """
        allowed_values = ["NOT_AVAILABLE", "REDUNDANT", "NOT_REDUNDANT_SINGLE_IPSEC", "NOT_REDUNDANT_SINGLE_VIRTUALCIRCUIT", "NOT_REDUNDANT_MULTIPLE_IPSECS", "NOT_REDUNDANT_MULTIPLE_VIRTUALCIRCUITS", "NOT_REDUNDANT_MIX_CONNECTIONS", "NOT_REDUNDANT_NO_CONNECTION"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
