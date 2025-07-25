# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TermVersionSummary(object):
    """
    The model for the term version summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TermVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TermVersionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TermVersionSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this TermVersionSummary.
        :type display_name: str

        :param status:
            The value to assign to the status property of this TermVersionSummary.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TermVersionSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this TermVersionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TermVersionSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this TermVersionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this TermVersionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this TermVersionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TermVersionSummary.
        Unique OCID identifier for the term version.


        :return: The id of this TermVersionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TermVersionSummary.
        Unique OCID identifier for the term version.


        :param id: The id of this TermVersionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TermVersionSummary.
        The unique identifier for the compartment.


        :return: The compartment_id of this TermVersionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TermVersionSummary.
        The unique identifier for the compartment.


        :param compartment_id: The compartment_id of this TermVersionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TermVersionSummary.
        The name for the term version.


        :return: The display_name of this TermVersionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TermVersionSummary.
        The name for the term version.


        :param display_name: The display_name of this TermVersionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TermVersionSummary.
        The current status for the term version.


        :return: The status of this TermVersionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TermVersionSummary.
        The current status for the term version.


        :param status: The status of this TermVersionSummary.
        :type: str
        """
        self._status = status

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this TermVersionSummary.
        The current state for the Term version.


        :return: The lifecycle_state of this TermVersionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TermVersionSummary.
        The current state for the Term version.


        :param lifecycle_state: The lifecycle_state of this TermVersionSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this TermVersionSummary.
        The date and time the term version was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this TermVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TermVersionSummary.
        The date and time the term version was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this TermVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this TermVersionSummary.
        The date and time the time version was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this TermVersionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TermVersionSummary.
        The date and time the time version was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this TermVersionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this TermVersionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this TermVersionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this TermVersionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this TermVersionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this TermVersionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this TermVersionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this TermVersionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this TermVersionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this TermVersionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this TermVersionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this TermVersionSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this TermVersionSummary.
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
