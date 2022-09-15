# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_environment import TargetEnvironment
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmTargetEnvironment(TargetEnvironment):
    """
    Description of the VM target environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmTargetEnvironment object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.VmTargetEnvironment.target_environment_type` attribute
        of this class is ``VM_TARGET_ENV`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this VmTargetEnvironment.
        :type target_compartment_id: str

        :param target_environment_type:
            The value to assign to the target_environment_type property of this VmTargetEnvironment.
            Allowed values for this property are: "VM_TARGET_ENV"
        :type target_environment_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this VmTargetEnvironment.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this VmTargetEnvironment.
        :type fault_domain: str

        :param vcn:
            The value to assign to the vcn property of this VmTargetEnvironment.
        :type vcn: str

        :param subnet:
            The value to assign to the subnet property of this VmTargetEnvironment.
        :type subnet: str

        :param dedicated_vm_host:
            The value to assign to the dedicated_vm_host property of this VmTargetEnvironment.
        :type dedicated_vm_host: str

        :param ms_license:
            The value to assign to the ms_license property of this VmTargetEnvironment.
        :type ms_license: str

        :param preferred_shape_type:
            The value to assign to the preferred_shape_type property of this VmTargetEnvironment.
        :type preferred_shape_type: str

        """
        self.swagger_types = {
            'target_compartment_id': 'str',
            'target_environment_type': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'vcn': 'str',
            'subnet': 'str',
            'dedicated_vm_host': 'str',
            'ms_license': 'str',
            'preferred_shape_type': 'str'
        }

        self.attribute_map = {
            'target_compartment_id': 'targetCompartmentId',
            'target_environment_type': 'targetEnvironmentType',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'vcn': 'vcn',
            'subnet': 'subnet',
            'dedicated_vm_host': 'dedicatedVmHost',
            'ms_license': 'msLicense',
            'preferred_shape_type': 'preferredShapeType'
        }

        self._target_compartment_id = None
        self._target_environment_type = None
        self._availability_domain = None
        self._fault_domain = None
        self._vcn = None
        self._subnet = None
        self._dedicated_vm_host = None
        self._ms_license = None
        self._preferred_shape_type = None
        self._target_environment_type = 'VM_TARGET_ENV'

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this VmTargetEnvironment.
        Availability Domain of the VM configuration.


        :return: The availability_domain of this VmTargetEnvironment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VmTargetEnvironment.
        Availability Domain of the VM configuration.


        :param availability_domain: The availability_domain of this VmTargetEnvironment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this VmTargetEnvironment.
        Fault domain of the VM configuration.


        :return: The fault_domain of this VmTargetEnvironment.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this VmTargetEnvironment.
        Fault domain of the VM configuration.


        :param fault_domain: The fault_domain of this VmTargetEnvironment.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def vcn(self):
        """
        **[Required]** Gets the vcn of this VmTargetEnvironment.
        OCID of the VM configuration VCN.


        :return: The vcn of this VmTargetEnvironment.
        :rtype: str
        """
        return self._vcn

    @vcn.setter
    def vcn(self, vcn):
        """
        Sets the vcn of this VmTargetEnvironment.
        OCID of the VM configuration VCN.


        :param vcn: The vcn of this VmTargetEnvironment.
        :type: str
        """
        self._vcn = vcn

    @property
    def subnet(self):
        """
        **[Required]** Gets the subnet of this VmTargetEnvironment.
        OCID of the VM configuration subnet.


        :return: The subnet of this VmTargetEnvironment.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """
        Sets the subnet of this VmTargetEnvironment.
        OCID of the VM configuration subnet.


        :param subnet: The subnet of this VmTargetEnvironment.
        :type: str
        """
        self._subnet = subnet

    @property
    def dedicated_vm_host(self):
        """
        Gets the dedicated_vm_host of this VmTargetEnvironment.
        OCID of the dedicated VM configuration host.


        :return: The dedicated_vm_host of this VmTargetEnvironment.
        :rtype: str
        """
        return self._dedicated_vm_host

    @dedicated_vm_host.setter
    def dedicated_vm_host(self, dedicated_vm_host):
        """
        Sets the dedicated_vm_host of this VmTargetEnvironment.
        OCID of the dedicated VM configuration host.


        :param dedicated_vm_host: The dedicated_vm_host of this VmTargetEnvironment.
        :type: str
        """
        self._dedicated_vm_host = dedicated_vm_host

    @property
    def ms_license(self):
        """
        Gets the ms_license of this VmTargetEnvironment.
        Microsoft license for the VM configuration.


        :return: The ms_license of this VmTargetEnvironment.
        :rtype: str
        """
        return self._ms_license

    @ms_license.setter
    def ms_license(self, ms_license):
        """
        Sets the ms_license of this VmTargetEnvironment.
        Microsoft license for the VM configuration.


        :param ms_license: The ms_license of this VmTargetEnvironment.
        :type: str
        """
        self._ms_license = ms_license

    @property
    def preferred_shape_type(self):
        """
        Gets the preferred_shape_type of this VmTargetEnvironment.
        Preferred VM shape type provided by the customer.


        :return: The preferred_shape_type of this VmTargetEnvironment.
        :rtype: str
        """
        return self._preferred_shape_type

    @preferred_shape_type.setter
    def preferred_shape_type(self, preferred_shape_type):
        """
        Sets the preferred_shape_type of this VmTargetEnvironment.
        Preferred VM shape type provided by the customer.


        :param preferred_shape_type: The preferred_shape_type of this VmTargetEnvironment.
        :type: str
        """
        self._preferred_shape_type = preferred_shape_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
