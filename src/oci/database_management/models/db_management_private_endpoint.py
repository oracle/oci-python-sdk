# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbManagementPrivateEndpoint(object):
    """
    A Database Management private endpoint allows Database Management to connect to databases in a Virtual Cloud Network (VCN).
    """

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbManagementPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbManagementPrivateEndpoint.
        :type id: str

        :param name:
            The value to assign to the name property of this DbManagementPrivateEndpoint.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbManagementPrivateEndpoint.
        :type compartment_id: str

        :param is_cluster:
            The value to assign to the is_cluster property of this DbManagementPrivateEndpoint.
        :type is_cluster: bool

        :param vcn_id:
            The value to assign to the vcn_id property of this DbManagementPrivateEndpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DbManagementPrivateEndpoint.
        :type subnet_id: str

        :param private_ip:
            The value to assign to the private_ip property of this DbManagementPrivateEndpoint.
        :type private_ip: str

        :param description:
            The value to assign to the description property of this DbManagementPrivateEndpoint.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DbManagementPrivateEndpoint.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbManagementPrivateEndpoint.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DbManagementPrivateEndpoint.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'is_cluster': 'bool',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_ip': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'is_cluster': 'isCluster',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_ip': 'privateIp',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'nsg_ids': 'nsgIds'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._is_cluster = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_ip = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._nsg_ids = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the Database Management private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the Database Management private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DbManagementPrivateEndpoint.
        The display name of the Database Management private endpoint.


        :return: The name of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DbManagementPrivateEndpoint.
        The display name of the Database Management private endpoint.


        :param name: The name of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this DbManagementPrivateEndpoint.
        Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.


        :return: The is_cluster of this DbManagementPrivateEndpoint.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this DbManagementPrivateEndpoint.
        Specifies whether the Database Management private endpoint can be used for Oracle Databases in a cluster.


        :param is_cluster: The is_cluster of this DbManagementPrivateEndpoint.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DbManagementPrivateEndpoint.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_ip(self):
        """
        Gets the private_ip of this DbManagementPrivateEndpoint.
        The IP addresses assigned to the Database Management private endpoint.


        :return: The private_ip of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this DbManagementPrivateEndpoint.
        The IP addresses assigned to the Database Management private endpoint.


        :param private_ip: The private_ip of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def description(self):
        """
        Gets the description of this DbManagementPrivateEndpoint.
        The description of the Database Management private endpoint.


        :return: The description of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DbManagementPrivateEndpoint.
        The description of the Database Management private endpoint.


        :param description: The description of this DbManagementPrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this DbManagementPrivateEndpoint.
        The date and time the Database Managament private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DbManagementPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbManagementPrivateEndpoint.
        The date and time the Database Managament private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DbManagementPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbManagementPrivateEndpoint.
        The current lifecycle state of the Database Management private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbManagementPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbManagementPrivateEndpoint.
        The current lifecycle state of the Database Management private endpoint.


        :param lifecycle_state: The lifecycle_state of this DbManagementPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DbManagementPrivateEndpoint.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :return: The nsg_ids of this DbManagementPrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DbManagementPrivateEndpoint.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :param nsg_ids: The nsg_ids of this DbManagementPrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
