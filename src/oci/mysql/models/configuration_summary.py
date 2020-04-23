# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationSummary(object):
    """
    The general details of a Configuration such as its id, displayName, type, and shape association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConfigurationSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConfigurationSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this ConfigurationSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ConfigurationSummary.
        :type display_name: str

        :param shape_name:
            The value to assign to the shape_name property of this ConfigurationSummary.
        :type shape_name: str

        :param type:
            The value to assign to the type property of this ConfigurationSummary.
        :type type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConfigurationSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ConfigurationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConfigurationSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConfigurationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'display_name': 'str',
            'shape_name': 'str',
            'type': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'display_name': 'displayName',
            'shape_name': 'shapeName',
            'type': 'type',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._description = None
        self._display_name = None
        self._shape_name = None
        self._type = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConfigurationSummary.
        The OCID of the Configuration.


        :return: The id of this ConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConfigurationSummary.
        The OCID of the Configuration.


        :param id: The id of this ConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConfigurationSummary.
        OCID of the Compartment the Configuration exists in.


        :return: The compartment_id of this ConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConfigurationSummary.
        OCID of the Compartment the Configuration exists in.


        :param compartment_id: The compartment_id of this ConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this ConfigurationSummary.
        User-provided data about the Configuration.


        :return: The description of this ConfigurationSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationSummary.
        User-provided data about the Configuration.


        :param description: The description of this ConfigurationSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this ConfigurationSummary.
        The display name of the Configuration.


        :return: The display_name of this ConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConfigurationSummary.
        The display name of the Configuration.


        :param display_name: The display_name of this ConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this ConfigurationSummary.
        The name of the associated Shape.


        :return: The shape_name of this ConfigurationSummary.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this ConfigurationSummary.
        The name of the associated Shape.


        :param shape_name: The shape_name of this ConfigurationSummary.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ConfigurationSummary.
        The Configuration type, DEFAULT or CUSTOM


        :return: The type of this ConfigurationSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConfigurationSummary.
        The Configuration type, DEFAULT or CUSTOM


        :param type: The type of this ConfigurationSummary.
        :type: str
        """
        self._type = type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConfigurationSummary.
        The current state of the Configuration.


        :return: The lifecycle_state of this ConfigurationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConfigurationSummary.
        The current state of the Configuration.


        :param lifecycle_state: The lifecycle_state of this ConfigurationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this ConfigurationSummary.
        The date and time the Configuration was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConfigurationSummary.
        The date and time the Configuration was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ConfigurationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ConfigurationSummary.
        The date and time the Configuration was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this ConfigurationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConfigurationSummary.
        The date and time the Configuration was last updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this ConfigurationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConfigurationSummary.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ConfigurationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConfigurationSummary.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ConfigurationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConfigurationSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ConfigurationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConfigurationSummary.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ConfigurationSummary.
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
