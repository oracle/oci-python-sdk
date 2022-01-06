# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TemplateSummary(object):
    """
    Summary information for a template.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TemplateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TemplateSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TemplateSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this TemplateSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TemplateSummary.
        :type description: str

        :param is_free_tier:
            The value to assign to the is_free_tier property of this TemplateSummary.
        :type is_free_tier: bool

        :param time_created:
            The value to assign to the time_created property of this TemplateSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TemplateSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'is_free_tier': 'bool',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'is_free_tier': 'isFreeTier',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._is_free_tier = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        Gets the id of this TemplateSummary.
        Unique identifier of the specified template.


        :return: The id of this TemplateSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemplateSummary.
        Unique identifier of the specified template.


        :param id: The id of this TemplateSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TemplateSummary.
        The `OCID`__ of the compartment containing this template.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this TemplateSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TemplateSummary.
        The `OCID`__ of the compartment containing this template.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this TemplateSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this TemplateSummary.
        Human-readable display name for the template.


        :return: The display_name of this TemplateSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TemplateSummary.
        Human-readable display name for the template.


        :param display_name: The display_name of this TemplateSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this TemplateSummary.
        Brief description of the template.


        :return: The description of this TemplateSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TemplateSummary.
        Brief description of the template.


        :param description: The description of this TemplateSummary.
        :type: str
        """
        self._description = description

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this TemplateSummary.
        whether the template will work for free tier tenancy.


        :return: The is_free_tier of this TemplateSummary.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this TemplateSummary.
        whether the template will work for free tier tenancy.


        :param is_free_tier: The is_free_tier of this TemplateSummary.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def time_created(self):
        """
        Gets the time_created of this TemplateSummary.
        The date and time at which the template was created.
        Format is defined by RFC3339.
        Example: `2020-11-25T21:10:29.600Z`


        :return: The time_created of this TemplateSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TemplateSummary.
        The date and time at which the template was created.
        Format is defined by RFC3339.
        Example: `2020-11-25T21:10:29.600Z`


        :param time_created: The time_created of this TemplateSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TemplateSummary.
        The current lifecycle state of the template.
        Allowable values:
        - ACTIVE


        :return: The lifecycle_state of this TemplateSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TemplateSummary.
        The current lifecycle state of the template.
        Allowable values:
        - ACTIVE


        :param lifecycle_state: The lifecycle_state of this TemplateSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
