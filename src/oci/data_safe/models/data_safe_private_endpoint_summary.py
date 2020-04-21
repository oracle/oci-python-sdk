# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSafePrivateEndpointSummary(object):
    """
    Summary of a Data Safe private endpoint.
    """

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataSafePrivateEndpointSummary.
    #: This constant has a value of "NA"
    LIFECYCLE_STATE_NA = "NA"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSafePrivateEndpointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataSafePrivateEndpointSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DataSafePrivateEndpointSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DataSafePrivateEndpointSummary.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this DataSafePrivateEndpointSummary.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DataSafePrivateEndpointSummary.
        :type subnet_id: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this DataSafePrivateEndpointSummary.
        :type private_endpoint_id: str

        :param description:
            The value to assign to the description property of this DataSafePrivateEndpointSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DataSafePrivateEndpointSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataSafePrivateEndpointSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_endpoint_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_endpoint_id': 'privateEndpointId',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_endpoint_id = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataSafePrivateEndpointSummary.
        The OCID of the Data Safe private endpoint.


        :return: The id of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataSafePrivateEndpointSummary.
        The OCID of the Data Safe private endpoint.


        :param id: The id of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DataSafePrivateEndpointSummary.
        The display name of the private endpoint.


        :return: The display_name of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataSafePrivateEndpointSummary.
        The display name of the private endpoint.


        :param display_name: The display_name of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DataSafePrivateEndpointSummary.
        The OCID of the compartment.


        :return: The compartment_id of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DataSafePrivateEndpointSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DataSafePrivateEndpointSummary.
        The OCID of the VCN.


        :return: The vcn_id of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DataSafePrivateEndpointSummary.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DataSafePrivateEndpointSummary.
        The OCID of the subnet.


        :return: The subnet_id of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DataSafePrivateEndpointSummary.
        The OCID of the subnet.


        :param subnet_id: The subnet_id of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_id(self):
        """
        **[Required]** Gets the private_endpoint_id of this DataSafePrivateEndpointSummary.
        The OCID of the private endpoint.


        :return: The private_endpoint_id of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this DataSafePrivateEndpointSummary.
        The OCID of the private endpoint.


        :param private_endpoint_id: The private_endpoint_id of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def description(self):
        """
        Gets the description of this DataSafePrivateEndpointSummary.
        The description of the private endpoint.


        :return: The description of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataSafePrivateEndpointSummary.
        The description of the private endpoint.


        :param description: The description of this DataSafePrivateEndpointSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this DataSafePrivateEndpointSummary.
        The date and time the private endpoint was created, in the format defined by RFC3339.


        :return: The time_created of this DataSafePrivateEndpointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataSafePrivateEndpointSummary.
        The date and time the private endpoint was created, in the format defined by RFC3339.


        :param time_created: The time_created of this DataSafePrivateEndpointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataSafePrivateEndpointSummary.
        The current state of the private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataSafePrivateEndpointSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataSafePrivateEndpointSummary.
        The current state of the private endpoint.


        :param lifecycle_state: The lifecycle_state of this DataSafePrivateEndpointSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA"]
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
