# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdpGroupMapping(object):
    """
    A mapping between a single group defined by the identity provider (IdP) you're federating with
    and a single IAM Service :class:`Group` in Oracle Cloud Infrastructure.
    For more information about group mappings and what they're for, see
    `Identity Providers and Federation`__.

    A given IdP group can be mapped to zero, one, or multiple IAM Service groups, and vice versa.
    But each `IdPGroupMapping` object is between only a single IdP group and IAM Service group.
    Each `IdPGroupMapping` object has its own OCID.

    **Note:** Any users who are in more than 50 IdP groups cannot be authenticated to use the Oracle
    Cloud Infrastructure Console.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/federation.htm
    """

    #: A constant which can be used with the lifecycle_state property of a IdpGroupMapping.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IdpGroupMapping.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IdpGroupMapping.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IdpGroupMapping.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IdpGroupMapping.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new IdpGroupMapping object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IdpGroupMapping.
        :type id: str

        :param idp_id:
            The value to assign to the idp_id property of this IdpGroupMapping.
        :type idp_id: str

        :param idp_group_name:
            The value to assign to the idp_group_name property of this IdpGroupMapping.
        :type idp_group_name: str

        :param group_id:
            The value to assign to the group_id property of this IdpGroupMapping.
        :type group_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IdpGroupMapping.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this IdpGroupMapping.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IdpGroupMapping.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this IdpGroupMapping.
        :type inactive_status: int

        """
        self.swagger_types = {
            'id': 'str',
            'idp_id': 'str',
            'idp_group_name': 'str',
            'group_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'idp_id': 'idpId',
            'idp_group_name': 'idpGroupName',
            'group_id': 'groupId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._idp_id = None
        self._idp_group_name = None
        self._group_id = None
        self._compartment_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IdpGroupMapping.
        The OCID of the `IdpGroupMapping`.


        :return: The id of this IdpGroupMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IdpGroupMapping.
        The OCID of the `IdpGroupMapping`.


        :param id: The id of this IdpGroupMapping.
        :type: str
        """
        self._id = id

    @property
    def idp_id(self):
        """
        **[Required]** Gets the idp_id of this IdpGroupMapping.
        The OCID of the `IdentityProvider` this mapping belongs to.


        :return: The idp_id of this IdpGroupMapping.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        """
        Sets the idp_id of this IdpGroupMapping.
        The OCID of the `IdentityProvider` this mapping belongs to.


        :param idp_id: The idp_id of this IdpGroupMapping.
        :type: str
        """
        self._idp_id = idp_id

    @property
    def idp_group_name(self):
        """
        **[Required]** Gets the idp_group_name of this IdpGroupMapping.
        The name of the IdP group that is mapped to the IAM Service group.


        :return: The idp_group_name of this IdpGroupMapping.
        :rtype: str
        """
        return self._idp_group_name

    @idp_group_name.setter
    def idp_group_name(self, idp_group_name):
        """
        Sets the idp_group_name of this IdpGroupMapping.
        The name of the IdP group that is mapped to the IAM Service group.


        :param idp_group_name: The idp_group_name of this IdpGroupMapping.
        :type: str
        """
        self._idp_group_name = idp_group_name

    @property
    def group_id(self):
        """
        **[Required]** Gets the group_id of this IdpGroupMapping.
        The OCID of the IAM Service group that is mapped to the IdP group.


        :return: The group_id of this IdpGroupMapping.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this IdpGroupMapping.
        The OCID of the IAM Service group that is mapped to the IdP group.


        :param group_id: The group_id of this IdpGroupMapping.
        :type: str
        """
        self._group_id = group_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IdpGroupMapping.
        The OCID of the tenancy containing the `IdentityProvider`.


        :return: The compartment_id of this IdpGroupMapping.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IdpGroupMapping.
        The OCID of the tenancy containing the `IdentityProvider`.


        :param compartment_id: The compartment_id of this IdpGroupMapping.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this IdpGroupMapping.
        Date and time the mapping was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IdpGroupMapping.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IdpGroupMapping.
        Date and time the mapping was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IdpGroupMapping.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this IdpGroupMapping.
        The mapping's current state.  After creating a mapping object, make sure its `lifecycleState` changes
        from CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IdpGroupMapping.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IdpGroupMapping.
        The mapping's current state.  After creating a mapping object, make sure its `lifecycleState` changes
        from CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this IdpGroupMapping.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this IdpGroupMapping.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this IdpGroupMapping.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this IdpGroupMapping.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this IdpGroupMapping.
        :type: int
        """
        self._inactive_status = inactive_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
