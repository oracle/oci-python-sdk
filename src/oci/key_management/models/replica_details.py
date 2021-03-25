# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicaDetails(object):
    """
    Details of replication status
    """

    #: A constant which can be used with the status property of a ReplicaDetails.
    #: This constant has a value of "REPLICATING"
    STATUS_REPLICATING = "REPLICATING"

    #: A constant which can be used with the status property of a ReplicaDetails.
    #: This constant has a value of "REPLICATED"
    STATUS_REPLICATED = "REPLICATED"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region:
            The value to assign to the region property of this ReplicaDetails.
        :type region: str

        :param status:
            The value to assign to the status property of this ReplicaDetails.
            Allowed values for this property are: "REPLICATING", "REPLICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'region': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'region': 'region',
            'status': 'status'
        }

        self._region = None
        self._status = None

    @property
    def region(self):
        """
        Gets the region of this ReplicaDetails.
        The replica region


        :return: The region of this ReplicaDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this ReplicaDetails.
        The replica region


        :param region: The region of this ReplicaDetails.
        :type: str
        """
        self._region = region

    @property
    def status(self):
        """
        Gets the status of this ReplicaDetails.
        Replication status associated with a replicationId

        Allowed values for this property are: "REPLICATING", "REPLICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ReplicaDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ReplicaDetails.
        Replication status associated with a replicationId


        :param status: The status of this ReplicaDetails.
        :type: str
        """
        allowed_values = ["REPLICATING", "REPLICATED"]
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
