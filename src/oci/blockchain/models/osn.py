# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Osn(object):
    """
    An Ordering Service Node details
    """

    #: A constant which can be used with the lifecycle_state property of a Osn.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Osn.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Osn.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Osn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param osn_key:
            The value to assign to the osn_key property of this Osn.
        :type osn_key: str

        :param ad:
            The value to assign to the ad property of this Osn.
        :type ad: str

        :param ocpu_allocation_param:
            The value to assign to the ocpu_allocation_param property of this Osn.
        :type ocpu_allocation_param: oci.blockchain.models.OcpuAllocationNumberParam

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Osn.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'osn_key': 'str',
            'ad': 'str',
            'ocpu_allocation_param': 'OcpuAllocationNumberParam',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'osn_key': 'osnKey',
            'ad': 'ad',
            'ocpu_allocation_param': 'ocpuAllocationParam',
            'lifecycle_state': 'lifecycleState'
        }

        self._osn_key = None
        self._ad = None
        self._ocpu_allocation_param = None
        self._lifecycle_state = None

    @property
    def osn_key(self):
        """
        **[Required]** Gets the osn_key of this Osn.
        OSN identifier


        :return: The osn_key of this Osn.
        :rtype: str
        """
        return self._osn_key

    @osn_key.setter
    def osn_key(self, osn_key):
        """
        Sets the osn_key of this Osn.
        OSN identifier


        :param osn_key: The osn_key of this Osn.
        :type: str
        """
        self._osn_key = osn_key

    @property
    def ad(self):
        """
        **[Required]** Gets the ad of this Osn.
        Availability Domain of OSN


        :return: The ad of this Osn.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this Osn.
        Availability Domain of OSN


        :param ad: The ad of this Osn.
        :type: str
        """
        self._ad = ad

    @property
    def ocpu_allocation_param(self):
        """
        Gets the ocpu_allocation_param of this Osn.

        :return: The ocpu_allocation_param of this Osn.
        :rtype: oci.blockchain.models.OcpuAllocationNumberParam
        """
        return self._ocpu_allocation_param

    @ocpu_allocation_param.setter
    def ocpu_allocation_param(self, ocpu_allocation_param):
        """
        Sets the ocpu_allocation_param of this Osn.

        :param ocpu_allocation_param: The ocpu_allocation_param of this Osn.
        :type: oci.blockchain.models.OcpuAllocationNumberParam
        """
        self._ocpu_allocation_param = ocpu_allocation_param

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Osn.
        The current state of the OSN.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Osn.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Osn.
        The current state of the OSN.


        :param lifecycle_state: The lifecycle_state of this Osn.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
