# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DedicatedVmHostSummary(object):
    """
    A dedicated virtual machine (VM) host lets you host multiple instances on a dedicated server that is not shared with other tenancies.
    """

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DedicatedVmHostSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DedicatedVmHostSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this DedicatedVmHostSummary.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DedicatedVmHostSummary.
        :type compartment_id: str

        :param dedicated_vm_host_shape:
            The value to assign to the dedicated_vm_host_shape property of this DedicatedVmHostSummary.
        :type dedicated_vm_host_shape: str

        :param display_name:
            The value to assign to the display_name property of this DedicatedVmHostSummary.
        :type display_name: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DedicatedVmHostSummary.
        :type fault_domain: str

        :param id:
            The value to assign to the id property of this DedicatedVmHostSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DedicatedVmHostSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DedicatedVmHostSummary.
        :type time_created: datetime

        :param remaining_ocpus:
            The value to assign to the remaining_ocpus property of this DedicatedVmHostSummary.
        :type remaining_ocpus: float

        :param total_ocpus:
            The value to assign to the total_ocpus property of this DedicatedVmHostSummary.
        :type total_ocpus: float

        :param total_memory_in_gbs:
            The value to assign to the total_memory_in_gbs property of this DedicatedVmHostSummary.
        :type total_memory_in_gbs: float

        :param remaining_memory_in_gbs:
            The value to assign to the remaining_memory_in_gbs property of this DedicatedVmHostSummary.
        :type remaining_memory_in_gbs: float

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'dedicated_vm_host_shape': 'str',
            'display_name': 'str',
            'fault_domain': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'remaining_ocpus': 'float',
            'total_ocpus': 'float',
            'total_memory_in_gbs': 'float',
            'remaining_memory_in_gbs': 'float'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'dedicated_vm_host_shape': 'dedicatedVmHostShape',
            'display_name': 'displayName',
            'fault_domain': 'faultDomain',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'remaining_ocpus': 'remainingOcpus',
            'total_ocpus': 'totalOcpus',
            'total_memory_in_gbs': 'totalMemoryInGBs',
            'remaining_memory_in_gbs': 'remainingMemoryInGBs'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._dedicated_vm_host_shape = None
        self._display_name = None
        self._fault_domain = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._remaining_ocpus = None
        self._total_ocpus = None
        self._total_memory_in_gbs = None
        self._remaining_memory_in_gbs = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this DedicatedVmHostSummary.
        The availability domain the dedicated VM host is running in.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DedicatedVmHostSummary.
        The availability domain the dedicated VM host is running in.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this DedicatedVmHostSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DedicatedVmHostSummary.
        The OCID of the compartment that contains the dedicated VM host.


        :return: The compartment_id of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DedicatedVmHostSummary.
        The OCID of the compartment that contains the dedicated VM host.


        :param compartment_id: The compartment_id of this DedicatedVmHostSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def dedicated_vm_host_shape(self):
        """
        **[Required]** Gets the dedicated_vm_host_shape of this DedicatedVmHostSummary.
        The shape of the dedicated VM host. The shape determines the number of CPUs and
        other resources available for VMs.


        :return: The dedicated_vm_host_shape of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._dedicated_vm_host_shape

    @dedicated_vm_host_shape.setter
    def dedicated_vm_host_shape(self, dedicated_vm_host_shape):
        """
        Sets the dedicated_vm_host_shape of this DedicatedVmHostSummary.
        The shape of the dedicated VM host. The shape determines the number of CPUs and
        other resources available for VMs.


        :param dedicated_vm_host_shape: The dedicated_vm_host_shape of this DedicatedVmHostSummary.
        :type: str
        """
        self._dedicated_vm_host_shape = dedicated_vm_host_shape

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DedicatedVmHostSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DedicatedVmHostSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this DedicatedVmHostSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this DedicatedVmHostSummary.
        The fault domain for the dedicated VM host's assigned instances. For more information, see Fault Domains.

        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated VM host,
        delete it and create a new dedicated VM host in the preferred fault domain.

        To get a list of fault domains, use the ListFaultDomains operation in the Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :return: The fault_domain of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DedicatedVmHostSummary.
        The fault domain for the dedicated VM host's assigned instances. For more information, see Fault Domains.

        If you do not specify the fault domain, the system selects one for you. To change the fault domain for a dedicated VM host,
        delete it and create a new dedicated VM host in the preferred fault domain.

        To get a list of fault domains, use the ListFaultDomains operation in the Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :param fault_domain: The fault_domain of this DedicatedVmHostSummary.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DedicatedVmHostSummary.
        The `OCID`__ of the dedicated VM host.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DedicatedVmHostSummary.
        The `OCID`__ of the dedicated VM host.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DedicatedVmHostSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DedicatedVmHostSummary.
        The current state of the dedicated VM host.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DedicatedVmHostSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DedicatedVmHostSummary.
        The current state of the dedicated VM host.


        :param lifecycle_state: The lifecycle_state of this DedicatedVmHostSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DedicatedVmHostSummary.
        The date and time the dedicated VM host was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DedicatedVmHostSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DedicatedVmHostSummary.
        The date and time the dedicated VM host was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DedicatedVmHostSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def remaining_ocpus(self):
        """
        **[Required]** Gets the remaining_ocpus of this DedicatedVmHostSummary.
        The current available OCPUs of the dedicated VM host.


        :return: The remaining_ocpus of this DedicatedVmHostSummary.
        :rtype: float
        """
        return self._remaining_ocpus

    @remaining_ocpus.setter
    def remaining_ocpus(self, remaining_ocpus):
        """
        Sets the remaining_ocpus of this DedicatedVmHostSummary.
        The current available OCPUs of the dedicated VM host.


        :param remaining_ocpus: The remaining_ocpus of this DedicatedVmHostSummary.
        :type: float
        """
        self._remaining_ocpus = remaining_ocpus

    @property
    def total_ocpus(self):
        """
        **[Required]** Gets the total_ocpus of this DedicatedVmHostSummary.
        The current total OCPUs of the dedicated VM host.


        :return: The total_ocpus of this DedicatedVmHostSummary.
        :rtype: float
        """
        return self._total_ocpus

    @total_ocpus.setter
    def total_ocpus(self, total_ocpus):
        """
        Sets the total_ocpus of this DedicatedVmHostSummary.
        The current total OCPUs of the dedicated VM host.


        :param total_ocpus: The total_ocpus of this DedicatedVmHostSummary.
        :type: float
        """
        self._total_ocpus = total_ocpus

    @property
    def total_memory_in_gbs(self):
        """
        Gets the total_memory_in_gbs of this DedicatedVmHostSummary.
        The current total memory of the dedicated VM host, in GBs.


        :return: The total_memory_in_gbs of this DedicatedVmHostSummary.
        :rtype: float
        """
        return self._total_memory_in_gbs

    @total_memory_in_gbs.setter
    def total_memory_in_gbs(self, total_memory_in_gbs):
        """
        Sets the total_memory_in_gbs of this DedicatedVmHostSummary.
        The current total memory of the dedicated VM host, in GBs.


        :param total_memory_in_gbs: The total_memory_in_gbs of this DedicatedVmHostSummary.
        :type: float
        """
        self._total_memory_in_gbs = total_memory_in_gbs

    @property
    def remaining_memory_in_gbs(self):
        """
        Gets the remaining_memory_in_gbs of this DedicatedVmHostSummary.
        The current available memory of the dedicated VM host, in GBs.


        :return: The remaining_memory_in_gbs of this DedicatedVmHostSummary.
        :rtype: float
        """
        return self._remaining_memory_in_gbs

    @remaining_memory_in_gbs.setter
    def remaining_memory_in_gbs(self, remaining_memory_in_gbs):
        """
        Sets the remaining_memory_in_gbs of this DedicatedVmHostSummary.
        The current available memory of the dedicated VM host, in GBs.


        :param remaining_memory_in_gbs: The remaining_memory_in_gbs of this DedicatedVmHostSummary.
        :type: float
        """
        self._remaining_memory_in_gbs = remaining_memory_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
