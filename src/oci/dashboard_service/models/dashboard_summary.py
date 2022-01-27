# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DashboardSummary(object):
    """
    Summary information about the dashboard.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DashboardSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DashboardSummary.
        :type id: str

        :param dashboard_group_id:
            The value to assign to the dashboard_group_id property of this DashboardSummary.
        :type dashboard_group_id: str

        :param display_name:
            The value to assign to the display_name property of this DashboardSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DashboardSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DashboardSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DashboardSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DashboardSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DashboardSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DashboardSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DashboardSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DashboardSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'dashboard_group_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'dashboard_group_id': 'dashboardGroupId',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._dashboard_group_id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DashboardSummary.
        The `OCID`__ of the dashboard resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this DashboardSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DashboardSummary.
        The `OCID`__ of the dashboard resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this DashboardSummary.
        :type: str
        """
        self._id = id

    @property
    def dashboard_group_id(self):
        """
        **[Required]** Gets the dashboard_group_id of this DashboardSummary.
        The `OCID`__ of the dashboard group that the dashboard belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The dashboard_group_id of this DashboardSummary.
        :rtype: str
        """
        return self._dashboard_group_id

    @dashboard_group_id.setter
    def dashboard_group_id(self, dashboard_group_id):
        """
        Sets the dashboard_group_id of this DashboardSummary.
        The `OCID`__ of the dashboard group that the dashboard belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param dashboard_group_id: The dashboard_group_id of this DashboardSummary.
        :type: str
        """
        self._dashboard_group_id = dashboard_group_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DashboardSummary.
        A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
        Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\


        :return: The display_name of this DashboardSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DashboardSummary.
        A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
        Leading and trailing spaces and the following special characters are not allowed: <>()=/'\"&\\


        :param display_name: The display_name of this DashboardSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this DashboardSummary.
        A short description of the dashboard. It can be changed. Avoid entering confidential information.
        The following special characters are not allowed: <>()=/'\"&\\


        :return: The description of this DashboardSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DashboardSummary.
        A short description of the dashboard. It can be changed. Avoid entering confidential information.
        The following special characters are not allowed: <>()=/'\"&\\


        :param description: The description of this DashboardSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DashboardSummary.
        The `OCID`__ of the compartment containing the dashboard. A dashboard is always in the same compartment as its dashboard group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DashboardSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DashboardSummary.
        The `OCID`__ of the compartment containing the dashboard. A dashboard is always in the same compartment as its dashboard group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DashboardSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DashboardSummary.
        The date and time the dashboard was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DashboardSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DashboardSummary.
        The date and time the dashboard was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DashboardSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DashboardSummary.
        The date and time the dashboard was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DashboardSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DashboardSummary.
        The date and time the dashboard was updated, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DashboardSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DashboardSummary.
        The current state of the Dashboard.


        :return: The lifecycle_state of this DashboardSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DashboardSummary.
        The current state of the Dashboard.


        :param lifecycle_state: The lifecycle_state of this DashboardSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this DashboardSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DashboardSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DashboardSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DashboardSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this DashboardSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DashboardSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DashboardSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DashboardSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DashboardSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DashboardSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DashboardSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DashboardSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
