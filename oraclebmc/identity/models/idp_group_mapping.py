# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class IdpGroupMapping(object):

    def __init__(self):

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
        Gets the id of this IdpGroupMapping.
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
        Gets the idp_id of this IdpGroupMapping.
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
        Gets the idp_group_name of this IdpGroupMapping.
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
        Gets the group_id of this IdpGroupMapping.
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
        Gets the compartment_id of this IdpGroupMapping.
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
        Gets the time_created of this IdpGroupMapping.
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
        Gets the lifecycle_state of this IdpGroupMapping.
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
        if lifecycle_state not in allowed_values:
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
