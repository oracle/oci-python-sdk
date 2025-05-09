# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedVmHostInstanceSummary(object):
    """
    Condensed instance data when listing instances on a dedicated VM host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedVmHostInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DedicatedVmHostInstanceSummary.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedVmHostInstanceSummary.
        :type compartment_id: str

        :param instance_id:
            The value to assign to the instance_id property of this DedicatedVmHostInstanceSummary.
        :type instance_id: str

        :param shape:
            The value to assign to the shape property of this DedicatedVmHostInstanceSummary.
        :type shape: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedVmHostInstanceSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'instance_id': 'str',
            'shape': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'instance_id': 'instanceId',
            'shape': 'shape',
            'time_created': 'timeCreated'
        }
        self._availability_domain = None
        self._compartment_id = None
        self._instance_id = None
        self._shape = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DedicatedVmHostInstanceSummary.
        The availability domain the virtual machine instance is running in.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this DedicatedVmHostInstanceSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DedicatedVmHostInstanceSummary.
        The availability domain the virtual machine instance is running in.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this DedicatedVmHostInstanceSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DedicatedVmHostInstanceSummary.
        The OCID of the compartment that contains the virtual machine instance.


        :return: The compartment_id of this DedicatedVmHostInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DedicatedVmHostInstanceSummary.
        The OCID of the compartment that contains the virtual machine instance.


        :param compartment_id: The compartment_id of this DedicatedVmHostInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this DedicatedVmHostInstanceSummary.
        The OCID of the virtual machine instance.


        :return: The instance_id of this DedicatedVmHostInstanceSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this DedicatedVmHostInstanceSummary.
        The OCID of the virtual machine instance.


        :param instance_id: The instance_id of this DedicatedVmHostInstanceSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this DedicatedVmHostInstanceSummary.
        The shape of the VM instance.


        :return: The shape of this DedicatedVmHostInstanceSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DedicatedVmHostInstanceSummary.
        The shape of the VM instance.


        :param shape: The shape of this DedicatedVmHostInstanceSummary.
        :type: str
        """
        self._shape = shape

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DedicatedVmHostInstanceSummary.
        The date and time the virtual machine instance was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DedicatedVmHostInstanceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DedicatedVmHostInstanceSummary.
        The date and time the virtual machine instance was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DedicatedVmHostInstanceSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
