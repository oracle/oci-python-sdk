# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileSummary(object):
    """
    The metadata associated with the profile summary.
    """

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ProfileSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProfileSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProfileSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this ProfileSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this ProfileSummary.
        :type description: str

        :param aggregation_interval_in_days:
            The value to assign to the aggregation_interval_in_days property of this ProfileSummary.
        :type aggregation_interval_in_days: int

        :param defined_tags:
            The value to assign to the defined_tags property of this ProfileSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProfileSummary.
        :type freeform_tags: dict(str, str)

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProfileSummary.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param levels_configuration:
            The value to assign to the levels_configuration property of this ProfileSummary.
        :type levels_configuration: oci.optimizer.models.LevelsConfiguration

        :param target_compartments:
            The value to assign to the target_compartments property of this ProfileSummary.
        :type target_compartments: oci.optimizer.models.TargetCompartments

        :param target_tags:
            The value to assign to the target_tags property of this ProfileSummary.
        :type target_tags: oci.optimizer.models.TargetTags

        :param time_created:
            The value to assign to the time_created property of this ProfileSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProfileSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'aggregation_interval_in_days': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'lifecycle_state': 'str',
            'levels_configuration': 'LevelsConfiguration',
            'target_compartments': 'TargetCompartments',
            'target_tags': 'TargetTags',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'aggregation_interval_in_days': 'aggregationIntervalInDays',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'lifecycle_state': 'lifecycleState',
            'levels_configuration': 'levelsConfiguration',
            'target_compartments': 'targetCompartments',
            'target_tags': 'targetTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._aggregation_interval_in_days = None
        self._defined_tags = None
        self._freeform_tags = None
        self._lifecycle_state = None
        self._levels_configuration = None
        self._target_compartments = None
        self._target_tags = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProfileSummary.
        The unique OCID of the profile.


        :return: The id of this ProfileSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProfileSummary.
        The unique OCID of the profile.


        :param id: The id of this ProfileSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProfileSummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :return: The compartment_id of this ProfileSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProfileSummary.
        The OCID of the tenancy. The tenancy is the root compartment.


        :param compartment_id: The compartment_id of this ProfileSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ProfileSummary.
        The name assigned to the profile.


        :return: The name of this ProfileSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProfileSummary.
        The name assigned to the profile.


        :param name: The name of this ProfileSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ProfileSummary.
        Text describing the profile.


        :return: The description of this ProfileSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProfileSummary.
        Text describing the profile.


        :param description: The description of this ProfileSummary.
        :type: str
        """
        self._description = description

    @property
    def aggregation_interval_in_days(self):
        """
        Gets the aggregation_interval_in_days of this ProfileSummary.
        The time period over which to collect data for the recommendations, measured in number of days.


        :return: The aggregation_interval_in_days of this ProfileSummary.
        :rtype: int
        """
        return self._aggregation_interval_in_days

    @aggregation_interval_in_days.setter
    def aggregation_interval_in_days(self, aggregation_interval_in_days):
        """
        Sets the aggregation_interval_in_days of this ProfileSummary.
        The time period over which to collect data for the recommendations, measured in number of days.


        :param aggregation_interval_in_days: The aggregation_interval_in_days of this ProfileSummary.
        :type: int
        """
        self._aggregation_interval_in_days = aggregation_interval_in_days

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ProfileSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ProfileSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProfileSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ProfileSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ProfileSummary.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ProfileSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProfileSummary.
        Simple key-value pair applied without any predefined name, type, or namespace.
        For more information, see `Resource Tags`__. Exists for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ProfileSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ProfileSummary.
        The profile's current state.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ProfileSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProfileSummary.
        The profile's current state.


        :param lifecycle_state: The lifecycle_state of this ProfileSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def levels_configuration(self):
        """
        Gets the levels_configuration of this ProfileSummary.

        :return: The levels_configuration of this ProfileSummary.
        :rtype: oci.optimizer.models.LevelsConfiguration
        """
        return self._levels_configuration

    @levels_configuration.setter
    def levels_configuration(self, levels_configuration):
        """
        Sets the levels_configuration of this ProfileSummary.

        :param levels_configuration: The levels_configuration of this ProfileSummary.
        :type: oci.optimizer.models.LevelsConfiguration
        """
        self._levels_configuration = levels_configuration

    @property
    def target_compartments(self):
        """
        Gets the target_compartments of this ProfileSummary.

        :return: The target_compartments of this ProfileSummary.
        :rtype: oci.optimizer.models.TargetCompartments
        """
        return self._target_compartments

    @target_compartments.setter
    def target_compartments(self, target_compartments):
        """
        Sets the target_compartments of this ProfileSummary.

        :param target_compartments: The target_compartments of this ProfileSummary.
        :type: oci.optimizer.models.TargetCompartments
        """
        self._target_compartments = target_compartments

    @property
    def target_tags(self):
        """
        Gets the target_tags of this ProfileSummary.

        :return: The target_tags of this ProfileSummary.
        :rtype: oci.optimizer.models.TargetTags
        """
        return self._target_tags

    @target_tags.setter
    def target_tags(self, target_tags):
        """
        Sets the target_tags of this ProfileSummary.

        :param target_tags: The target_tags of this ProfileSummary.
        :type: oci.optimizer.models.TargetTags
        """
        self._target_tags = target_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ProfileSummary.
        The date and time the profile was created, in the format defined by RFC3339.


        :return: The time_created of this ProfileSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProfileSummary.
        The date and time the profile was created, in the format defined by RFC3339.


        :param time_created: The time_created of this ProfileSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ProfileSummary.
        The date and time the profile was last updated, in the format defined by RFC3339.


        :return: The time_updated of this ProfileSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProfileSummary.
        The date and time the profile was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this ProfileSummary.
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
