# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VaultReplicaSummary(object):
    """
    Summary of vault replicas
    """

    #: A constant which can be used with the status property of a VaultReplicaSummary.
    #: This constant has a value of "CREATING"
    STATUS_CREATING = "CREATING"

    #: A constant which can be used with the status property of a VaultReplicaSummary.
    #: This constant has a value of "CREATED"
    STATUS_CREATED = "CREATED"

    #: A constant which can be used with the status property of a VaultReplicaSummary.
    #: This constant has a value of "DELETING"
    STATUS_DELETING = "DELETING"

    #: A constant which can be used with the status property of a VaultReplicaSummary.
    #: This constant has a value of "DELETED"
    STATUS_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new VaultReplicaSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param crypto_endpoint:
            The value to assign to the crypto_endpoint property of this VaultReplicaSummary.
        :type crypto_endpoint: str

        :param management_endpoint:
            The value to assign to the management_endpoint property of this VaultReplicaSummary.
        :type management_endpoint: str

        :param region:
            The value to assign to the region property of this VaultReplicaSummary.
        :type region: str

        :param status:
            The value to assign to the status property of this VaultReplicaSummary.
            Allowed values for this property are: "CREATING", "CREATED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'crypto_endpoint': 'str',
            'management_endpoint': 'str',
            'region': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'crypto_endpoint': 'cryptoEndpoint',
            'management_endpoint': 'managementEndpoint',
            'region': 'region',
            'status': 'status'
        }

        self._crypto_endpoint = None
        self._management_endpoint = None
        self._region = None
        self._status = None

    @property
    def crypto_endpoint(self):
        """
        Gets the crypto_endpoint of this VaultReplicaSummary.
        The vault replica's crypto endpoint


        :return: The crypto_endpoint of this VaultReplicaSummary.
        :rtype: str
        """
        return self._crypto_endpoint

    @crypto_endpoint.setter
    def crypto_endpoint(self, crypto_endpoint):
        """
        Sets the crypto_endpoint of this VaultReplicaSummary.
        The vault replica's crypto endpoint


        :param crypto_endpoint: The crypto_endpoint of this VaultReplicaSummary.
        :type: str
        """
        self._crypto_endpoint = crypto_endpoint

    @property
    def management_endpoint(self):
        """
        Gets the management_endpoint of this VaultReplicaSummary.
        The vault replica's management endpoint


        :return: The management_endpoint of this VaultReplicaSummary.
        :rtype: str
        """
        return self._management_endpoint

    @management_endpoint.setter
    def management_endpoint(self, management_endpoint):
        """
        Sets the management_endpoint of this VaultReplicaSummary.
        The vault replica's management endpoint


        :param management_endpoint: The management_endpoint of this VaultReplicaSummary.
        :type: str
        """
        self._management_endpoint = management_endpoint

    @property
    def region(self):
        """
        Gets the region of this VaultReplicaSummary.
        Region to which vault is replicated to


        :return: The region of this VaultReplicaSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this VaultReplicaSummary.
        Region to which vault is replicated to


        :param region: The region of this VaultReplicaSummary.
        :type: str
        """
        self._region = region

    @property
    def status(self):
        """
        Gets the status of this VaultReplicaSummary.
        Allowed values for this property are: "CREATING", "CREATED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this VaultReplicaSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VaultReplicaSummary.

        :param status: The status of this VaultReplicaSummary.
        :type: str
        """
        allowed_values = ["CREATING", "CREATED", "DELETING", "DELETED"]
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
