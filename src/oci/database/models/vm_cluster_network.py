# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmClusterNetwork(object):
    """
    The VM cluster network.
    """

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "REQUIRES_VALIDATION"
    LIFECYCLE_STATE_REQUIRES_VALIDATION = "REQUIRES_VALIDATION"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "VALIDATING"
    LIFECYCLE_STATE_VALIDATING = "VALIDATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "VALIDATED"
    LIFECYCLE_STATE_VALIDATED = "VALIDATED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "VALIDATION_FAILED"
    LIFECYCLE_STATE_VALIDATION_FAILED = "VALIDATION_FAILED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "ALLOCATED"
    LIFECYCLE_STATE_ALLOCATED = "ALLOCATED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterNetwork.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new VmClusterNetwork object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VmClusterNetwork.
        :type id: str

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this VmClusterNetwork.
        :type exadata_infrastructure_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VmClusterNetwork.
        :type compartment_id: str

        :param vm_cluster_id:
            The value to assign to the vm_cluster_id property of this VmClusterNetwork.
        :type vm_cluster_id: str

        :param display_name:
            The value to assign to the display_name property of this VmClusterNetwork.
        :type display_name: str

        :param scans:
            The value to assign to the scans property of this VmClusterNetwork.
        :type scans: list[oci.database.models.ScanDetails]

        :param dns:
            The value to assign to the dns property of this VmClusterNetwork.
        :type dns: list[str]

        :param ntp:
            The value to assign to the ntp property of this VmClusterNetwork.
        :type ntp: list[str]

        :param vm_networks:
            The value to assign to the vm_networks property of this VmClusterNetwork.
        :type vm_networks: list[oci.database.models.VmNetworkDetails]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmClusterNetwork.
            Allowed values for this property are: "CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this VmClusterNetwork.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmClusterNetwork.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VmClusterNetwork.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VmClusterNetwork.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'exadata_infrastructure_id': 'str',
            'compartment_id': 'str',
            'vm_cluster_id': 'str',
            'display_name': 'str',
            'scans': 'list[ScanDetails]',
            'dns': 'list[str]',
            'ntp': 'list[str]',
            'vm_networks': 'list[VmNetworkDetails]',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'compartment_id': 'compartmentId',
            'vm_cluster_id': 'vmClusterId',
            'display_name': 'displayName',
            'scans': 'scans',
            'dns': 'dns',
            'ntp': 'ntp',
            'vm_networks': 'vmNetworks',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._exadata_infrastructure_id = None
        self._compartment_id = None
        self._vm_cluster_id = None
        self._display_name = None
        self._scans = None
        self._dns = None
        self._ntp = None
        self._vm_networks = None
        self._lifecycle_state = None
        self._time_created = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        Gets the id of this VmClusterNetwork.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this VmClusterNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VmClusterNetwork.
        The `OCID`__ of the VM cluster network.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this VmClusterNetwork.
        :type: str
        """
        self._id = id

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this VmClusterNetwork.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this VmClusterNetwork.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this VmClusterNetwork.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this VmClusterNetwork.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VmClusterNetwork.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this VmClusterNetwork.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VmClusterNetwork.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this VmClusterNetwork.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vm_cluster_id(self):
        """
        Gets the vm_cluster_id of this VmClusterNetwork.
        The `OCID`__ of the associated VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_id of this VmClusterNetwork.
        :rtype: str
        """
        return self._vm_cluster_id

    @vm_cluster_id.setter
    def vm_cluster_id(self, vm_cluster_id):
        """
        Sets the vm_cluster_id of this VmClusterNetwork.
        The `OCID`__ of the associated VM Cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_id: The vm_cluster_id of this VmClusterNetwork.
        :type: str
        """
        self._vm_cluster_id = vm_cluster_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VmClusterNetwork.
        The user-friendly name for the VM cluster network. The name does not need to be unique.


        :return: The display_name of this VmClusterNetwork.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VmClusterNetwork.
        The user-friendly name for the VM cluster network. The name does not need to be unique.


        :param display_name: The display_name of this VmClusterNetwork.
        :type: str
        """
        self._display_name = display_name

    @property
    def scans(self):
        """
        Gets the scans of this VmClusterNetwork.
        The SCAN details.


        :return: The scans of this VmClusterNetwork.
        :rtype: list[oci.database.models.ScanDetails]
        """
        return self._scans

    @scans.setter
    def scans(self, scans):
        """
        Sets the scans of this VmClusterNetwork.
        The SCAN details.


        :param scans: The scans of this VmClusterNetwork.
        :type: list[oci.database.models.ScanDetails]
        """
        self._scans = scans

    @property
    def dns(self):
        """
        Gets the dns of this VmClusterNetwork.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :return: The dns of this VmClusterNetwork.
        :rtype: list[str]
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """
        Sets the dns of this VmClusterNetwork.
        The list of DNS server IP addresses. Maximum of 3 allowed.


        :param dns: The dns of this VmClusterNetwork.
        :type: list[str]
        """
        self._dns = dns

    @property
    def ntp(self):
        """
        Gets the ntp of this VmClusterNetwork.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :return: The ntp of this VmClusterNetwork.
        :rtype: list[str]
        """
        return self._ntp

    @ntp.setter
    def ntp(self, ntp):
        """
        Sets the ntp of this VmClusterNetwork.
        The list of NTP server IP addresses. Maximum of 3 allowed.


        :param ntp: The ntp of this VmClusterNetwork.
        :type: list[str]
        """
        self._ntp = ntp

    @property
    def vm_networks(self):
        """
        Gets the vm_networks of this VmClusterNetwork.
        Details of the client and backup networks.


        :return: The vm_networks of this VmClusterNetwork.
        :rtype: list[oci.database.models.VmNetworkDetails]
        """
        return self._vm_networks

    @vm_networks.setter
    def vm_networks(self, vm_networks):
        """
        Sets the vm_networks of this VmClusterNetwork.
        Details of the client and backup networks.


        :param vm_networks: The vm_networks of this VmClusterNetwork.
        :type: list[oci.database.models.VmNetworkDetails]
        """
        self._vm_networks = vm_networks

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VmClusterNetwork.
        The current state of the VM cluster network.
        CREATING - The resource is being created
        REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
        VALIDATING - The resource is being validated and not available to use.
        VALIDATED - The resource is validated and is available for consumption by VM cluster.
        VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
        UPDATING - The resource is being updated and not available to use.
        ALLOCATED - The resource is is currently being used by VM cluster.
        TERMINATING - The resource is being deleted and not available to use.
        TERMINATED - The resource is deleted and unavailable.
        FAILED - The resource is in a failed state due to validation or other errors.
        NEEDS_ATTENTION - The resource is in needs attention state as some of it's child nodes are not validated
                          and unusable by VM cluster.

        Allowed values for this property are: "CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VmClusterNetwork.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VmClusterNetwork.
        The current state of the VM cluster network.
        CREATING - The resource is being created
        REQUIRES_VALIDATION - The resource is created and may not be usable until it is validated.
        VALIDATING - The resource is being validated and not available to use.
        VALIDATED - The resource is validated and is available for consumption by VM cluster.
        VALIDATION_FAILED - The resource validation has failed and might require user input to be corrected.
        UPDATING - The resource is being updated and not available to use.
        ALLOCATED - The resource is is currently being used by VM cluster.
        TERMINATING - The resource is being deleted and not available to use.
        TERMINATED - The resource is deleted and unavailable.
        FAILED - The resource is in a failed state due to validation or other errors.
        NEEDS_ATTENTION - The resource is in needs attention state as some of it's child nodes are not validated
                          and unusable by VM cluster.


        :param lifecycle_state: The lifecycle_state of this VmClusterNetwork.
        :type: str
        """
        allowed_values = ["CREATING", "REQUIRES_VALIDATION", "VALIDATING", "VALIDATED", "VALIDATION_FAILED", "UPDATING", "ALLOCATED", "TERMINATING", "TERMINATED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this VmClusterNetwork.
        The date and time when the VM cluster network was created.


        :return: The time_created of this VmClusterNetwork.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VmClusterNetwork.
        The date and time when the VM cluster network was created.


        :param time_created: The time_created of this VmClusterNetwork.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this VmClusterNetwork.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this VmClusterNetwork.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this VmClusterNetwork.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this VmClusterNetwork.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VmClusterNetwork.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VmClusterNetwork.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VmClusterNetwork.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VmClusterNetwork.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VmClusterNetwork.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VmClusterNetwork.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VmClusterNetwork.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VmClusterNetwork.
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
