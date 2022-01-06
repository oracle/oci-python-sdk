# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDedicatedVmHostDetails(object):
    """
    The details for creating a new dedicated virtual machine host.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDedicatedVmHostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateDedicatedVmHostDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDedicatedVmHostDetails.
        :type compartment_id: str

        :param dedicated_vm_host_shape:
            The value to assign to the dedicated_vm_host_shape property of this CreateDedicatedVmHostDetails.
        :type dedicated_vm_host_shape: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDedicatedVmHostDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateDedicatedVmHostDetails.
        :type display_name: str

        :param fault_domain:
            The value to assign to the fault_domain property of this CreateDedicatedVmHostDetails.
        :type fault_domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDedicatedVmHostDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'dedicated_vm_host_shape': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'fault_domain': 'str',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'dedicated_vm_host_shape': 'dedicatedVmHostShape',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'fault_domain': 'faultDomain',
            'freeform_tags': 'freeformTags'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._dedicated_vm_host_shape = None
        self._defined_tags = None
        self._display_name = None
        self._fault_domain = None
        self._freeform_tags = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CreateDedicatedVmHostDetails.
        The availability domain of the dedicated virtual machine host.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateDedicatedVmHostDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateDedicatedVmHostDetails.
        The availability domain of the dedicated virtual machine host.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateDedicatedVmHostDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDedicatedVmHostDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateDedicatedVmHostDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDedicatedVmHostDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateDedicatedVmHostDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dedicated_vm_host_shape(self):
        """
        **[Required]** Gets the dedicated_vm_host_shape of this CreateDedicatedVmHostDetails.
        The dedicated virtual machine host shape. The shape determines the number of CPUs and
        other resources available for VM instances launched on the dedicated virtual machine host.


        :return: The dedicated_vm_host_shape of this CreateDedicatedVmHostDetails.
        :rtype: str
        """
        return self._dedicated_vm_host_shape

    @dedicated_vm_host_shape.setter
    def dedicated_vm_host_shape(self, dedicated_vm_host_shape):
        """
        Sets the dedicated_vm_host_shape of this CreateDedicatedVmHostDetails.
        The dedicated virtual machine host shape. The shape determines the number of CPUs and
        other resources available for VM instances launched on the dedicated virtual machine host.


        :param dedicated_vm_host_shape: The dedicated_vm_host_shape of this CreateDedicatedVmHostDetails.
        :type: str
        """
        self._dedicated_vm_host_shape = dedicated_vm_host_shape

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDedicatedVmHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDedicatedVmHostDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDedicatedVmHostDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDedicatedVmHostDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDedicatedVmHostDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateDedicatedVmHostDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDedicatedVmHostDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateDedicatedVmHostDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CreateDedicatedVmHostDetails.
        The fault domain for the dedicated virtual machine host's assigned instances.
        For more information, see `Fault Domains`__.
        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
        delete it and create a new dedicated virtual machine host in the preferred fault domain.

        To get a list of fault domains, use the `ListFaultDomains` operation in
        the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :return: The fault_domain of this CreateDedicatedVmHostDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CreateDedicatedVmHostDetails.
        The fault domain for the dedicated virtual machine host's assigned instances.
        For more information, see `Fault Domains`__.
        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
        delete it and create a new dedicated virtual machine host in the preferred fault domain.

        To get a list of fault domains, use the `ListFaultDomains` operation in
        the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :param fault_domain: The fault_domain of this CreateDedicatedVmHostDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDedicatedVmHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDedicatedVmHostDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDedicatedVmHostDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDedicatedVmHostDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
