# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PbfListingVersion(object):
    """
    This represents a version of a PbfListing. Each new update from the publisher or the change in the image will
    result in the creation of new PbfListingVersion resource creation. This is a sub-resource of a PbfListing.
    """

    #: A constant which can be used with the lifecycle_state property of a PbfListingVersion.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PbfListingVersion.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a PbfListingVersion.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new PbfListingVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PbfListingVersion.
        :type id: str

        :param pbf_listing_id:
            The value to assign to the pbf_listing_id property of this PbfListingVersion.
        :type pbf_listing_id: str

        :param name:
            The value to assign to the name property of this PbfListingVersion.
        :type name: str

        :param config:
            The value to assign to the config property of this PbfListingVersion.
        :type config: list[oci.functions.models.ConfigDetails]

        :param requirements:
            The value to assign to the requirements property of this PbfListingVersion.
        :type requirements: oci.functions.models.RequirementDetails

        :param change_summary:
            The value to assign to the change_summary property of this PbfListingVersion.
        :type change_summary: str

        :param triggers:
            The value to assign to the triggers property of this PbfListingVersion.
        :type triggers: list[oci.functions.models.Trigger]

        :param time_created:
            The value to assign to the time_created property of this PbfListingVersion.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PbfListingVersion.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PbfListingVersion.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PbfListingVersion.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PbfListingVersion.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PbfListingVersion.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'pbf_listing_id': 'str',
            'name': 'str',
            'config': 'list[ConfigDetails]',
            'requirements': 'RequirementDetails',
            'change_summary': 'str',
            'triggers': 'list[Trigger]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'pbf_listing_id': 'pbfListingId',
            'name': 'name',
            'config': 'config',
            'requirements': 'requirements',
            'change_summary': 'changeSummary',
            'triggers': 'triggers',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._pbf_listing_id = None
        self._name = None
        self._config = None
        self._requirements = None
        self._change_summary = None
        self._triggers = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PbfListingVersion.
        Unique identifier that is immutable on creation


        :return: The id of this PbfListingVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PbfListingVersion.
        Unique identifier that is immutable on creation


        :param id: The id of this PbfListingVersion.
        :type: str
        """
        self._id = id

    @property
    def pbf_listing_id(self):
        """
        **[Required]** Gets the pbf_listing_id of this PbfListingVersion.
        The OCID of the PbfListing this resource version belongs to.


        :return: The pbf_listing_id of this PbfListingVersion.
        :rtype: str
        """
        return self._pbf_listing_id

    @pbf_listing_id.setter
    def pbf_listing_id(self, pbf_listing_id):
        """
        Sets the pbf_listing_id of this PbfListingVersion.
        The OCID of the PbfListing this resource version belongs to.


        :param pbf_listing_id: The pbf_listing_id of this PbfListingVersion.
        :type: str
        """
        self._pbf_listing_id = pbf_listing_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PbfListingVersion.
        Semantic version


        :return: The name of this PbfListingVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PbfListingVersion.
        Semantic version


        :param name: The name of this PbfListingVersion.
        :type: str
        """
        self._name = name

    @property
    def config(self):
        """
        Gets the config of this PbfListingVersion.
        Details about the required and optional Function configurations needed for proper performance of the PBF.


        :return: The config of this PbfListingVersion.
        :rtype: list[oci.functions.models.ConfigDetails]
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this PbfListingVersion.
        Details about the required and optional Function configurations needed for proper performance of the PBF.


        :param config: The config of this PbfListingVersion.
        :type: list[oci.functions.models.ConfigDetails]
        """
        self._config = config

    @property
    def requirements(self):
        """
        **[Required]** Gets the requirements of this PbfListingVersion.

        :return: The requirements of this PbfListingVersion.
        :rtype: oci.functions.models.RequirementDetails
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """
        Sets the requirements of this PbfListingVersion.

        :param requirements: The requirements of this PbfListingVersion.
        :type: oci.functions.models.RequirementDetails
        """
        self._requirements = requirements

    @property
    def change_summary(self):
        """
        **[Required]** Gets the change_summary of this PbfListingVersion.
        Details changes are included in this version.


        :return: The change_summary of this PbfListingVersion.
        :rtype: str
        """
        return self._change_summary

    @change_summary.setter
    def change_summary(self, change_summary):
        """
        Sets the change_summary of this PbfListingVersion.
        Details changes are included in this version.


        :param change_summary: The change_summary of this PbfListingVersion.
        :type: str
        """
        self._change_summary = change_summary

    @property
    def triggers(self):
        """
        **[Required]** Gets the triggers of this PbfListingVersion.
        An array of Trigger. A list of triggers that may activate the PBF.


        :return: The triggers of this PbfListingVersion.
        :rtype: list[oci.functions.models.Trigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this PbfListingVersion.
        An array of Trigger. A list of triggers that may activate the PBF.


        :param triggers: The triggers of this PbfListingVersion.
        :type: list[oci.functions.models.Trigger]
        """
        self._triggers = triggers

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PbfListingVersion.
        The time the PbfListingVersion was created. An RFC3339 formatted datetime string.


        :return: The time_created of this PbfListingVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PbfListingVersion.
        The time the PbfListingVersion was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this PbfListingVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PbfListingVersion.
        The last time the PbfListingVersion was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this PbfListingVersion.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PbfListingVersion.
        The last time the PbfListingVersion was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this PbfListingVersion.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PbfListingVersion.
        The current state of the PBF resource.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PbfListingVersion.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PbfListingVersion.
        The current state of the PBF resource.


        :param lifecycle_state: The lifecycle_state of this PbfListingVersion.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PbfListingVersion.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PbfListingVersion.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PbfListingVersion.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PbfListingVersion.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PbfListingVersion.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PbfListingVersion.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PbfListingVersion.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PbfListingVersion.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PbfListingVersion.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PbfListingVersion.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PbfListingVersion.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PbfListingVersion.
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
