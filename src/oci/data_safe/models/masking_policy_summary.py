# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingPolicySummary(object):
    """
    Summary of a masking policy.
    """

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a MaskingPolicySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingPolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MaskingPolicySummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MaskingPolicySummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MaskingPolicySummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this MaskingPolicySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MaskingPolicySummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MaskingPolicySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param description:
            The value to assign to the description property of this MaskingPolicySummary.
        :type description: str

        :param column_source:
            The value to assign to the column_source property of this MaskingPolicySummary.
        :type column_source: oci.data_safe.models.ColumnSourceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MaskingPolicySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MaskingPolicySummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'description': 'str',
            'column_source': 'ColumnSourceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'description': 'description',
            'column_source': 'columnSource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._description = None
        self._column_source = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MaskingPolicySummary.
        The OCID of the masking policy.


        :return: The id of this MaskingPolicySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaskingPolicySummary.
        The OCID of the masking policy.


        :param id: The id of this MaskingPolicySummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MaskingPolicySummary.
        The OCID of the compartment that contains the masking policy.


        :return: The compartment_id of this MaskingPolicySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MaskingPolicySummary.
        The OCID of the compartment that contains the masking policy.


        :param compartment_id: The compartment_id of this MaskingPolicySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MaskingPolicySummary.
        The display name of the masking policy.


        :return: The display_name of this MaskingPolicySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MaskingPolicySummary.
        The display name of the masking policy.


        :param display_name: The display_name of this MaskingPolicySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MaskingPolicySummary.
        The date and time the masking policy was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MaskingPolicySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MaskingPolicySummary.
        The date and time the masking policy was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MaskingPolicySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this MaskingPolicySummary.
        The date and time the masking policy was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this MaskingPolicySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MaskingPolicySummary.
        The date and time the masking policy was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this MaskingPolicySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MaskingPolicySummary.
        The current state of the masking policy.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MaskingPolicySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MaskingPolicySummary.
        The current state of the masking policy.


        :param lifecycle_state: The lifecycle_state of this MaskingPolicySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def description(self):
        """
        Gets the description of this MaskingPolicySummary.
        The description of the masking policy.


        :return: The description of this MaskingPolicySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MaskingPolicySummary.
        The description of the masking policy.


        :param description: The description of this MaskingPolicySummary.
        :type: str
        """
        self._description = description

    @property
    def column_source(self):
        """
        Gets the column_source of this MaskingPolicySummary.

        :return: The column_source of this MaskingPolicySummary.
        :rtype: oci.data_safe.models.ColumnSourceDetails
        """
        return self._column_source

    @column_source.setter
    def column_source(self, column_source):
        """
        Sets the column_source of this MaskingPolicySummary.

        :param column_source: The column_source of this MaskingPolicySummary.
        :type: oci.data_safe.models.ColumnSourceDetails
        """
        self._column_source = column_source

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MaskingPolicySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MaskingPolicySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MaskingPolicySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MaskingPolicySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MaskingPolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MaskingPolicySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MaskingPolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MaskingPolicySummary.
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
