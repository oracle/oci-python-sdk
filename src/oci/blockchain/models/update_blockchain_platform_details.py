# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBlockchainPlatformDetails(object):
    """
    Blockchain Platform details for updating a service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBlockchainPlatformDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateBlockchainPlatformDetails.
        :type description: str

        :param storage_size_in_tbs:
            The value to assign to the storage_size_in_tbs property of this UpdateBlockchainPlatformDetails.
        :type storage_size_in_tbs: float

        :param replicas:
            The value to assign to the replicas property of this UpdateBlockchainPlatformDetails.
        :type replicas: oci.blockchain.models.ReplicaDetails

        :param total_ocpu_capacity:
            The value to assign to the total_ocpu_capacity property of this UpdateBlockchainPlatformDetails.
        :type total_ocpu_capacity: int

        :param load_balancer_shape:
            The value to assign to the load_balancer_shape property of this UpdateBlockchainPlatformDetails.
        :type load_balancer_shape: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBlockchainPlatformDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBlockchainPlatformDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'storage_size_in_tbs': 'float',
            'replicas': 'ReplicaDetails',
            'total_ocpu_capacity': 'int',
            'load_balancer_shape': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'storage_size_in_tbs': 'storageSizeInTBs',
            'replicas': 'replicas',
            'total_ocpu_capacity': 'totalOcpuCapacity',
            'load_balancer_shape': 'loadBalancerShape',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._storage_size_in_tbs = None
        self._replicas = None
        self._total_ocpu_capacity = None
        self._load_balancer_shape = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateBlockchainPlatformDetails.
        Platform Description


        :return: The description of this UpdateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateBlockchainPlatformDetails.
        Platform Description


        :param description: The description of this UpdateBlockchainPlatformDetails.
        :type: str
        """
        self._description = description

    @property
    def storage_size_in_tbs(self):
        """
        Gets the storage_size_in_tbs of this UpdateBlockchainPlatformDetails.
        Storage size in TBs


        :return: The storage_size_in_tbs of this UpdateBlockchainPlatformDetails.
        :rtype: float
        """
        return self._storage_size_in_tbs

    @storage_size_in_tbs.setter
    def storage_size_in_tbs(self, storage_size_in_tbs):
        """
        Sets the storage_size_in_tbs of this UpdateBlockchainPlatformDetails.
        Storage size in TBs


        :param storage_size_in_tbs: The storage_size_in_tbs of this UpdateBlockchainPlatformDetails.
        :type: float
        """
        self._storage_size_in_tbs = storage_size_in_tbs

    @property
    def replicas(self):
        """
        Gets the replicas of this UpdateBlockchainPlatformDetails.

        :return: The replicas of this UpdateBlockchainPlatformDetails.
        :rtype: oci.blockchain.models.ReplicaDetails
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this UpdateBlockchainPlatformDetails.

        :param replicas: The replicas of this UpdateBlockchainPlatformDetails.
        :type: oci.blockchain.models.ReplicaDetails
        """
        self._replicas = replicas

    @property
    def total_ocpu_capacity(self):
        """
        Gets the total_ocpu_capacity of this UpdateBlockchainPlatformDetails.
        Number of total OCPUs to allocate


        :return: The total_ocpu_capacity of this UpdateBlockchainPlatformDetails.
        :rtype: int
        """
        return self._total_ocpu_capacity

    @total_ocpu_capacity.setter
    def total_ocpu_capacity(self, total_ocpu_capacity):
        """
        Sets the total_ocpu_capacity of this UpdateBlockchainPlatformDetails.
        Number of total OCPUs to allocate


        :param total_ocpu_capacity: The total_ocpu_capacity of this UpdateBlockchainPlatformDetails.
        :type: int
        """
        self._total_ocpu_capacity = total_ocpu_capacity

    @property
    def load_balancer_shape(self):
        """
        Gets the load_balancer_shape of this UpdateBlockchainPlatformDetails.
        Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.


        :return: The load_balancer_shape of this UpdateBlockchainPlatformDetails.
        :rtype: str
        """
        return self._load_balancer_shape

    @load_balancer_shape.setter
    def load_balancer_shape(self, load_balancer_shape):
        """
        Sets the load_balancer_shape of this UpdateBlockchainPlatformDetails.
        Type of Load Balancer shape - LB_100_MBPS or LB_400_MBPS. Default is LB_100_MBPS.


        :param load_balancer_shape: The load_balancer_shape of this UpdateBlockchainPlatformDetails.
        :type: str
        """
        self._load_balancer_shape = load_balancer_shape

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBlockchainPlatformDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateBlockchainPlatformDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBlockchainPlatformDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateBlockchainPlatformDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBlockchainPlatformDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateBlockchainPlatformDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBlockchainPlatformDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateBlockchainPlatformDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
