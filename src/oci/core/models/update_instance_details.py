# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstanceDetails(object):
    """
    UpdateInstanceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateInstanceDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param metadata:
            The value to assign to the metadata property of this UpdateInstanceDetails.
        :type metadata: dict(str, str)

        :param extended_metadata:
            The value to assign to the extended_metadata property of this UpdateInstanceDetails.
        :type extended_metadata: dict(str, object)

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'metadata': 'dict(str, str)',
            'extended_metadata': 'dict(str, object)'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'metadata': 'metadata',
            'extended_metadata': 'extendedMetadata'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._metadata = None
        self._extended_metadata = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :return: The display_name of this UpdateInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :param display_name: The display_name of this UpdateInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateInstanceDetails.
        Custom metadata key/value string pairs that you provide. Any set of key/value pairs
        provided here will completely replace the current set of key/value pairs in the 'metadata'
        field on the instance.

        Both the 'user_data' and 'ssh_authorized_keys' fields cannot be changed after an instance
        has launched. Any request which updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for 'user_data' and 'ssh_authorized_keys' that
        already exist on the instance.


        :return: The metadata of this UpdateInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateInstanceDetails.
        Custom metadata key/value string pairs that you provide. Any set of key/value pairs
        provided here will completely replace the current set of key/value pairs in the 'metadata'
        field on the instance.

        Both the 'user_data' and 'ssh_authorized_keys' fields cannot be changed after an instance
        has launched. Any request which updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for 'user_data' and 'ssh_authorized_keys' that
        already exist on the instance.


        :param metadata: The metadata of this UpdateInstanceDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this UpdateInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects
        (whereas 'metadata' fields are string/string maps only).

        Both the 'user_data' and 'ssh_authorized_keys' fields cannot be changed after an instance
        has launched. Any request which updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for 'user_data' and 'ssh_authorized_keys' that
        already exist on the instance.


        :return: The extended_metadata of this UpdateInstanceDetails.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this UpdateInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects
        (whereas 'metadata' fields are string/string maps only).

        Both the 'user_data' and 'ssh_authorized_keys' fields cannot be changed after an instance
        has launched. Any request which updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for 'user_data' and 'ssh_authorized_keys' that
        already exist on the instance.


        :param extended_metadata: The extended_metadata of this UpdateInstanceDetails.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
