# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Organization(object):
    """
    An organization entity.
    """

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Organization.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Organization object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Organization.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Organization.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Organization.
        :type compartment_id: str

        :param parent_name:
            The value to assign to the parent_name property of this Organization.
        :type parent_name: str

        :param default_ucm_subscription_id:
            The value to assign to the default_ucm_subscription_id property of this Organization.
        :type default_ucm_subscription_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Organization.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Organization.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Organization.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'parent_name': 'str',
            'default_ucm_subscription_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'parent_name': 'parentName',
            'default_ucm_subscription_id': 'defaultUcmSubscriptionId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._parent_name = None
        self._default_ucm_subscription_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Organization.
        OCID of the organization.


        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Organization.
        OCID of the organization.


        :param id: The id of this Organization.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Organization.
        A display name for the organization. Avoid entering confidential information.


        :return: The display_name of this Organization.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Organization.
        A display name for the organization. Avoid entering confidential information.


        :param display_name: The display_name of this Organization.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Organization.
        OCID of the compartment containing the organization. Always a tenancy OCID.


        :return: The compartment_id of this Organization.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Organization.
        OCID of the compartment containing the organization. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this Organization.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def parent_name(self):
        """
        Gets the parent_name of this Organization.
        The name of the tenancy that is the organization parent.


        :return: The parent_name of this Organization.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """
        Sets the parent_name of this Organization.
        The name of the tenancy that is the organization parent.


        :param parent_name: The parent_name of this Organization.
        :type: str
        """
        self._parent_name = parent_name

    @property
    def default_ucm_subscription_id(self):
        """
        **[Required]** Gets the default_ucm_subscription_id of this Organization.
        OCID of the default Annual Universal Credits subscription. Any tenancy joining the organization will automatically get assigned this subscription if a subscription is not explictly assigned.


        :return: The default_ucm_subscription_id of this Organization.
        :rtype: str
        """
        return self._default_ucm_subscription_id

    @default_ucm_subscription_id.setter
    def default_ucm_subscription_id(self, default_ucm_subscription_id):
        """
        Sets the default_ucm_subscription_id of this Organization.
        OCID of the default Annual Universal Credits subscription. Any tenancy joining the organization will automatically get assigned this subscription if a subscription is not explictly assigned.


        :param default_ucm_subscription_id: The default_ucm_subscription_id of this Organization.
        :type: str
        """
        self._default_ucm_subscription_id = default_ucm_subscription_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Organization.
        Lifecycle state of the organization.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Organization.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Organization.
        Lifecycle state of the organization.


        :param lifecycle_state: The lifecycle_state of this Organization.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Organization.
        Date-time when this organization was created.


        :return: The time_created of this Organization.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Organization.
        Date-time when this organization was created.


        :param time_created: The time_created of this Organization.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Organization.
        Date-time when this organization was last updated.


        :return: The time_updated of this Organization.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Organization.
        Date-time when this organization was last updated.


        :param time_updated: The time_updated of this Organization.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
