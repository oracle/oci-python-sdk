# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedVmHost(object):
    """
    A dedicated virtual machine host that enables you to host multiple VM instances
    on a dedicated host that is not shared with other tenancies.
    """

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHost.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedVmHost object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DedicatedVmHost.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedVmHost.
        :type compartment_id: str

        :param dedicated_vm_host_shape:
            The value to assign to the dedicated_vm_host_shape property of this DedicatedVmHost.
        :type dedicated_vm_host_shape: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DedicatedVmHost.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DedicatedVmHost.
        :type display_name: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DedicatedVmHost.
        :type fault_domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DedicatedVmHost.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this DedicatedVmHost.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DedicatedVmHost.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedVmHost.
        :type time_created: datetime

        :param total_ocpus:
            The value to assign to the total_ocpus property of this DedicatedVmHost.
        :type total_ocpus: float

        :param remaining_ocpus:
            The value to assign to the remaining_ocpus property of this DedicatedVmHost.
        :type remaining_ocpus: float

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'dedicated_vm_host_shape': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'fault_domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'total_ocpus': 'float',
            'remaining_ocpus': 'float'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'dedicated_vm_host_shape': 'dedicatedVmHostShape',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'fault_domain': 'faultDomain',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'total_ocpus': 'totalOcpus',
            'remaining_ocpus': 'remainingOcpus'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._dedicated_vm_host_shape = None
        self._defined_tags = None
        self._display_name = None
        self._fault_domain = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._total_ocpus = None
        self._remaining_ocpus = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DedicatedVmHost.
        The availability domain the dedicated virtual machine host is running in.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this DedicatedVmHost.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DedicatedVmHost.
        The availability domain the dedicated virtual machine host is running in.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this DedicatedVmHost.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DedicatedVmHost.
        The OCID of the compartment that contains the dedicated virtual machine host.


        :return: The compartment_id of this DedicatedVmHost.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DedicatedVmHost.
        The OCID of the compartment that contains the dedicated virtual machine host.


        :param compartment_id: The compartment_id of this DedicatedVmHost.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dedicated_vm_host_shape(self):
        """
        **[Required]** Gets the dedicated_vm_host_shape of this DedicatedVmHost.
        The dedicated virtual machine host shape. The shape determines the number of CPUs and
        other resources available for VMs.


        :return: The dedicated_vm_host_shape of this DedicatedVmHost.
        :rtype: str
        """
        return self._dedicated_vm_host_shape

    @dedicated_vm_host_shape.setter
    def dedicated_vm_host_shape(self, dedicated_vm_host_shape):
        """
        Sets the dedicated_vm_host_shape of this DedicatedVmHost.
        The dedicated virtual machine host shape. The shape determines the number of CPUs and
        other resources available for VMs.


        :param dedicated_vm_host_shape: The dedicated_vm_host_shape of this DedicatedVmHost.
        :type: str
        """
        self._dedicated_vm_host_shape = dedicated_vm_host_shape

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DedicatedVmHost.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DedicatedVmHost.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DedicatedVmHost.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DedicatedVmHost.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DedicatedVmHost.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My Dedicated Vm Host`


        :return: The display_name of this DedicatedVmHost.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DedicatedVmHost.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My Dedicated Vm Host`


        :param display_name: The display_name of this DedicatedVmHost.
        :type: str
        """
        self._display_name = display_name

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this DedicatedVmHost.
        The fault domain for the dedicated virtual machine host's assigned instances.
        For more information, see `Fault Domains`__.

        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
        delete it, and then create a new dedicated virtual machine host in the preferred fault domain.

        To get a list of fault domains, use the `ListFaultDomains` operation in the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :return: The fault_domain of this DedicatedVmHost.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DedicatedVmHost.
        The fault domain for the dedicated virtual machine host's assigned instances.
        For more information, see `Fault Domains`__.

        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated virtual machine host,
        delete it, and then create a new dedicated virtual machine host in the preferred fault domain.

        To get a list of fault domains, use the `ListFaultDomains` operation in the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :param fault_domain: The fault_domain of this DedicatedVmHost.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DedicatedVmHost.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DedicatedVmHost.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DedicatedVmHost.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DedicatedVmHost.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DedicatedVmHost.
        The OCID of the dedicated VM host.


        :return: The id of this DedicatedVmHost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DedicatedVmHost.
        The OCID of the dedicated VM host.


        :param id: The id of this DedicatedVmHost.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DedicatedVmHost.
        The current state of the dedicated VM host.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DedicatedVmHost.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DedicatedVmHost.
        The current state of the dedicated VM host.


        :param lifecycle_state: The lifecycle_state of this DedicatedVmHost.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DedicatedVmHost.
        The date and time the dedicated VM host was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DedicatedVmHost.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DedicatedVmHost.
        The date and time the dedicated VM host was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DedicatedVmHost.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def total_ocpus(self):
        """
        **[Required]** Gets the total_ocpus of this DedicatedVmHost.
        The total OCPUs of the dedicated VM host.


        :return: The total_ocpus of this DedicatedVmHost.
        :rtype: float
        """
        return self._total_ocpus

    @total_ocpus.setter
    def total_ocpus(self, total_ocpus):
        """
        Sets the total_ocpus of this DedicatedVmHost.
        The total OCPUs of the dedicated VM host.


        :param total_ocpus: The total_ocpus of this DedicatedVmHost.
        :type: float
        """
        self._total_ocpus = total_ocpus

    @property
    def remaining_ocpus(self):
        """
        **[Required]** Gets the remaining_ocpus of this DedicatedVmHost.
        The available OCPUs of the dedicated VM host.


        :return: The remaining_ocpus of this DedicatedVmHost.
        :rtype: float
        """
        return self._remaining_ocpus

    @remaining_ocpus.setter
    def remaining_ocpus(self, remaining_ocpus):
        """
        Sets the remaining_ocpus of this DedicatedVmHost.
        The available OCPUs of the dedicated VM host.


        :param remaining_ocpus: The remaining_ocpus of this DedicatedVmHost.
        :type: float
        """
        self._remaining_ocpus = remaining_ocpus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
