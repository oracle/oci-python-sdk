# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationSummary(object):
    """
    Summary information for an instance configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfigurationSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this InstanceConfigurationSummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this InstanceConfigurationSummary.
        :type time_created: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConfigurationSummary.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'time_created': 'timeCreated',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._time_created = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this InstanceConfigurationSummary.
        The OCID of the compartment containing the instance configuration.


        :return: The compartment_id of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConfigurationSummary.
        The OCID of the compartment containing the instance configuration.


        :param compartment_id: The compartment_id of this InstanceConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationSummary.
        A user-friendly name for the instance configuration.


        :return: The display_name of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationSummary.
        A user-friendly name for the instance configuration.


        :param display_name: The display_name of this InstanceConfigurationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstanceConfigurationSummary.
        The OCID of the instance configuration.


        :return: The id of this InstanceConfigurationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceConfigurationSummary.
        The OCID of the instance configuration.


        :param id: The id of this InstanceConfigurationSummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this InstanceConfigurationSummary.
        The date and time the instance configuration was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this InstanceConfigurationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this InstanceConfigurationSummary.
        The date and time the instance configuration was created, in the format defined by `RFC3339`__.
        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this InstanceConfigurationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfigurationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConfigurationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfigurationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfigurationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfigurationSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConfigurationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
