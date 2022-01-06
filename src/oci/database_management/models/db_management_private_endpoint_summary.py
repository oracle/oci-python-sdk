# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbManagementPrivateEndpointSummary(object):
    """
    The summary of a Database Management private endpoint.
    """

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DbManagementPrivateEndpointSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbManagementPrivateEndpointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbManagementPrivateEndpointSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this DbManagementPrivateEndpointSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbManagementPrivateEndpointSummary.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this DbManagementPrivateEndpointSummary.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DbManagementPrivateEndpointSummary.
        :type subnet_id: str

        :param description:
            The value to assign to the description property of this DbManagementPrivateEndpointSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DbManagementPrivateEndpointSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbManagementPrivateEndpointSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the Database Management private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the Database Management private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DbManagementPrivateEndpointSummary.
        The display name of the Database Management private endpoint.


        :return: The name of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DbManagementPrivateEndpointSummary.
        The display name of the Database Management private endpoint.


        :param name: The name of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DbManagementPrivateEndpointSummary.
        The `OCID`__ of the subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def description(self):
        """
        Gets the description of this DbManagementPrivateEndpointSummary.
        The description of the private endpoint.


        :return: The description of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DbManagementPrivateEndpointSummary.
        The description of the private endpoint.


        :param description: The description of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this DbManagementPrivateEndpointSummary.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DbManagementPrivateEndpointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbManagementPrivateEndpointSummary.
        The date and time the private endpoint was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DbManagementPrivateEndpointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbManagementPrivateEndpointSummary.
        The current lifecycle state of the private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbManagementPrivateEndpointSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbManagementPrivateEndpointSummary.
        The current lifecycle state of the private endpoint.


        :param lifecycle_state: The lifecycle_state of this DbManagementPrivateEndpointSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
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
